import requests
import json
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform
from datetime import datetime


def get_data():
    # Get facebook status
    r = requests.patch('http://127.0.0.1:5000/cron')

    return 0