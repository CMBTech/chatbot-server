import requests
import json
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform
from datetime import datetime


def get_data():
    # Get facebook status
    r = requests.patch('https://internetstatus-iens.ue.r.appspot.com/cron')

    return 0