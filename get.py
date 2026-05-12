# get.py
import os
import logging
import redivis
logger = logging.getLogger(__name__)
REDIVIS_API_TOKEN = os.environ["REDIVIS_API_TOKEN"]
if not REDIVIS_API_TOKEN:
    raise RuntimeError("Missing REDIVIS_API_TOKEN environment variable.")
def get():
    
    logger.info('Getting notebooks from Redivis...')
    username = "opierce"
    workflow_name = "quarterly_by_city:pb7v"
    notebook_name = "quarterly_by_city:r3y8"
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    logger.info(f'Running {notebook_name} notebook finished.')
    # Wordpress triggers here or in Redivis notebook itself.
