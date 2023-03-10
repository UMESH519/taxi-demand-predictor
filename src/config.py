HOPSWORKS_PROJECT_NAME='taxi_demand_predictor'

import os
from dotenv import load_dotenv

from src.paths import PARENT_DIR
load_dotenv(PARENT_DIR / '.env')

HOPSWORKS_API_KEY = os.environ['HOPSWORKS_API_KEY']
FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1


FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1
FEATURE_VIEW_NAME = 'time_series_hourly_feature_view'
FEATURE_VIEW_VERSION = 1
MODEL_NAME = "taxi_demand_predictor_next_hour"
MODEL_VERSION = 1

N_FEATURES = 24 * 28