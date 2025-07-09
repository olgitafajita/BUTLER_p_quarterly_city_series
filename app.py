# app.py
import datetime
import get
import logging
import os
import time

logger = logging.getLogger(__name__)

# Timezone setup
os.environ['TZ'] = 'US/Pacific'
time.tzset()
now = datetime.datetime.now()

def main():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logger.info(f'Started at {now}')
    get.get()
    logger.info(f'Finished at {now}')

if __name__ == '__main__':
    main()