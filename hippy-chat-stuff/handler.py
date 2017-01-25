import arrow
import buzz
import json
import logging
import requests
import textwrap
import urllib


HIPCHAT_DEFAULT_TITLE = 'event occured in application'


class HipchatHandler(logging.Handler):
    """
    This module provides a logging handler that sends notifications to a
    hipchat room. The notifications will appear as expandable 'cards'
    with relevant data.

    .. todo:: Add sentry support for the card urls
    """

    def __init__(
            self, url, room, token, title=HIPCHAT_DEFAULT_TITLE,
            *args, **kwargs
    ):
        """
        Initializes the handler

        :param: url:   The base URL to the hipchat server
        :param: room:  The name of the room in which to make the notification
        :param: token: The auth token for the room
        :param: title: An optional title to include in the notification
        """

        self.url = '{url}/v2/room/{room}/notification'.format(
            url=url,
            room=urllib.parse.quote(room),
        )
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token),
        }
        self.title = title
        super().__init__(*args, **kwargs)

    def _make_payload(self, record):
        """
        Creates a payload for the room notification
        """
        html_title = '<b>{}</b> {}'.format(record.levelname, self.title)

        # Note: the description has to be 500 characters or less. Othewise
        #       hipchat will bounce the message
        description = textwrap.shorten(
            self.format(record),
            width=500,
            placeholder='...',
        )

        return json.dumps({
            "color": "red",
            "notify": True,
            "message_format": "html",
            "message": html_title,
            "card": {
                "id": str(arrow.get().timestamp),
                "style": "application",
                "format": "medium",
                "title": '{} {}'.format(record.levelname, self.title),
                "description": description,
                "url": 'https://some.sentry.server.someday',
                "activity": {"html": html_title},
            },
        })

    def emit(self, record):
        """
        Sends a notification to the hipchat room when a message is logged to
        the handler
        """
        response = requests.post(
            self.url, headers=self.headers, data=self._make_payload(record),
        )
        buzz.Buzz.require_condition(
            response is not None and response.status_code in (200, 204),
            "hipchat api did not accept the post: {}",
            str(response),
        )
