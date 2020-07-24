import logging
import psycopg2
import coloredlogs
from config import config

logging.basicConfig()
logger = logging.getLogger("poll-ooni")
logger.setLevel(logging.DEBUG)
coloredlogs.install()
coloredlogs.install(level='DEBUG')
conn = psycopg2.connect(**config['postgres'])

logger.info("Made connection to the database:",  conn.get_dsn_parameters())
cur = conn.cursor()
logger.debug("Made database cursor.")

create_fortiguard_table_command =  """
CREATE TABLE fortiguard_categories (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    fortiguard_category VARCHAR(255) NOT NULL
)
"""

cur.execute(create_fortiguard_table_command)
conn.commit()
logger.info("Created fortiguard_cateogries table")

logger.info("Done")
