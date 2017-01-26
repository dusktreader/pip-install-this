Overview
========

This package provides a logging handler that can send messages to a hipchat
room in the form of notifications.

It makes use of Hipchat's `API <https://www.hipchat.com/docs/apiv2>`_ to post
notifications to a hipchat server and room of your choosing.

The handler works like a standard logging handler, and may be set up with its
own formatter and log level.

Note that messages posted to the chat room can be at most 3 lines of text.
However, the notification can be supplied with a url link. This could be used
to show more information about the error such as with an error aggregator like
Sentry or to show the full log messages with a tool like Splunk.
