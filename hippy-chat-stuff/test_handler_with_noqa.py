import collections
import json
import logging
import pytest
import requests

from hippy_chat.handler import HipchatHandler, HIPCHAT_DEFAULT_TITLE


class TestHipchatHandler:

    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Sets up the logger for the tests in this class. Is automatically
        invoked before each test function is called
        """
        self.logger = logging.getLogger('TestHipchatLogger')
        self.logger.setLevel(logging.DEBUG)

    @pytest.yield_fixture
    def dummy_handler(self):
        """
        Provides a dummy instance of a HipchatHandler
        """
        dummy_url = 'https://some.fake.server.hipchat.com'
        dummy_room_name = 'some-room'
        dummy_token = 'SOME_TOKEN'

        dummy_handler = HipchatHandler(dummy_url, dummy_room_name, dummy_token)
        self.logger.addHandler(dummy_handler)
        yield dummy_handler
        self.logger.removeHandler(dummy_handler)

    def test___init__(self, dummy_handler):
        """
        This test verifies that a HipchatHandler instance can be initialized
        and that its url, headers, and title are properly set up based on the
        init params

        .. todo::
            check url formatting of weird room names
        """
        assert dummy_handler.url == (
            'https://some.fake.server.hipchat.com'
            '/v2/room/some-room/notification'
        )
        assert dummy_handler.headers == {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer SOME_TOKEN',
        }
        assert dummy_handler.title == HIPCHAT_DEFAULT_TITLE

    def test__make_payload(self, dummy_handler):
        """
        This test verifies that the data payload for the request that is sent
        to the hipchat API is properly constructed and encoded

        .. todo::
            * test long (>500 char) messages
            * test timestamp id
        """
        pass

    def test_integration(self, monkeypatch, dummy_handler):
        """
        This test verifies that the HipchatHandler integrates correctly with
        the logging module and that a request is posted to the hipchat api
        when a logging message at or above the level that the handler is
        initialized with
        """
        results = []

        def mock_post(url, headers=[], data={}):
            Result = collections.namedtuple('Result', ['status_code'])
            results.append(data)
            return Result(status_code=204)

        monkeypatch.setattr(requests, 'post', mock_post)

        self.logger.error("test error message")
        assert len(results) == 1
        result_data = results.pop()

        computed_data = json.loads(result_data)
        assert computed_data['color'] == 'red'
        assert computed_data['notify']
        assert computed_data['message'] == '<b>ERROR</b> {}'.format(HIPCHAT_DEFAULT_TITLE)  # noqa
