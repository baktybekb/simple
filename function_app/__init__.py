import os
import logging
import datetime

from pydantic import BaseModel
import azure.functions as func
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main(mytimer: func.TimerRequest) -> None:
    name = os.getenv('NAME')
    utc_timestamp = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f'Python timer trigger function ran at {utc_timestamp}. Name: {name}')
