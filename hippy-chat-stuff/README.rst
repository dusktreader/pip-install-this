************
 hippy-chat
************

----------------------------------
Hipchat logging handler for python
----------------------------------

This package provides a logging handler that can send messages to a hipchat
room in the form of notifications.

Requirements
============

 - Python 3

Installing
==========
Install using pip::

$ pip install hippy-chat

Using
=====
Setup the handler with the needed credentials for the hipchat server's api that
you will be sending messages to:

.. code-block:: python

   from hippy_chat.handler import HipchatHandler

   handler = HipchatHandler(
       'https://some_hipchat_server', 'some-room', 'SOME_HIPCHAT_API_TOKEN',
   )
   logger.addHandler(handler)

Contributing
============

In order to get your environment set up for development, it is recommended to
use virtualenv and pip to install dev dependencies::

    $ virtualenv --python=python3 env
    $ source env/bin/activate
    $ pip install -e .[dev]
