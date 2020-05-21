import logging
from database_client.database import Operations

def set_loggers():

    # set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] [%(name)-12s] [%(levelname)-6s] (%(message)s)',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


set_loggers()

logging.info('LOGGERS READY')

try:
    Operations.create_tables()
except Exception as e:
    logging.warning(e)
