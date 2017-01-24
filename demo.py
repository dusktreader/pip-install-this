import click

import hippy_chat.handler


@click.command()
@click.option('-c', '--config-file', help="the file containing hipchat deets")
@click.option(
    '-l', '--log-level',
    default='ERROR',
    type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    help="select the level of messges that should be logged to the room",
)
@click.option(
    '-i', '--message-interval',
    default=5,
    type=int,
    help="How often to message the room",
)
def main(config_file, log_level):

    log_level = getattr(logging, log_level)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    with open(os.path.expanduser('~/.hipchat.json')) as config_file:
        config = json.load(config_file)

    url = config['default_url']
    room = config['urls'][url]['default_room']
    token = config['urls'][url][room]['token']

    formatter = logging.Formatter(textwrap.dedent("""
        Severity: %(levelname)s
        Module:   %(module)s [%(pathname)s:%(lineno)d]
        Message: '%(message)s
    """))

    hipchat_handler = hippy_chat.handler.HipchatHandler(url, room, token)
    hipchat_handler.setLevel(log_level)
    hipchat_handler.setFormatter(formatter)

    logger.debug("This message should never appear in hipchat")
    logger.info("INFO level message")
    logger.warning("WARNING level message")
    logger.error("ERROR level message")
    logger.critical("CRITICAL level message")

    while True:
        logger.log(log_level, "The time is {}".format(arrow.get()))
        sleep(5)


if __name__ == '__main__':
    main()
