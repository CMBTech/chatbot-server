import requests
import json
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform
from datetime import datetime


def get_data():
    # Cron function to query endpoint that gets platform status
    r = requests.patch('https://internetstatus-iens.ue.r.appspot.com/cron')

    return 0