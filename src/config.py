HOPSWORKS_PROJECT_NAME='taxi_demand_predictor'

import os
from dotenv import load_dotenv

from src.paths import PARENT_DIR
load_dotenv(PARENT_DIR / '.env')

HOPSWORKS_API_KEY = os.environ['HOPSWORKS_API_KEY']
FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1