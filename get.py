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
    username = "glevines"
    workflow_name = "gva:kgtn"
    notebook_name = "gva_updater:x4bf"
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    logger.info(f'Running {notebook_name} notebook finished.')