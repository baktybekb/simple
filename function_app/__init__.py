import os
import logging
import datetime
from dotenv import load_dotenv
import azure.functions as func

# Load environment variables from .env file
load_dotenv()


def main(mytimer: func.TimerRequest) -> None:
    name = os.getenv('NAME')
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f'Python timer trigger function ran at {utc_timestamp}. Name: {name}')
