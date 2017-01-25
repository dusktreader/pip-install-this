import arrow
import click
import json
import logging
import os
import time
import hippy_chat.handler


@click.command()
@click.option(
    '-c', '--config-file',
    default='.hipchat.json',
    help="the file containing hipchat deets",
)
@click.option(
    '-l', '--log-level',
    default='ERROR',
    type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
    help="select the level of messges that should be logged to the room",
)
@click.option(
    '-i', '--message-interval',
    default=5,
    type=int,
    help="How often to message the room",
)
def main(config_file, log_level, message_interval):

    log_level = getattr(logging, log_level)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    with open(os.path.expanduser('.hipchat.json')) as config_file:
        config = json.load(config_file)
    hipchat_handler = hippy_chat.handler.HipchatHandler(**config)
    hipchat_handler.setLevel(log_level)

    logger.addHandler(hipchat_handler)

    logger.debug("DEBUG level message")
    logger.info("INFO level message")
    logger.warning("WARNING level message")
    logger.error("ERROR level message")
    logger.critical("CRITICAL level message")

    for i in range(5):
        logger.log(log_level, "The time is {}".format(arrow.get()))
        time.sleep(message_interval)


if __name__ == '__main__':
    main()
