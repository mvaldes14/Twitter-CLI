import yaml
import os

# Configuration from YAML
config_file = os.path.dirname(os.path.dirname(__file__))
with open(os.path.join(config_file, 'twitterConfig.yaml')) as f:
    config = yaml.load(f)

# Keys
CONSUMER_KEY = config['Twitter_API']['CONSUMER_KEY']
CONSUMER_SECRET = config['Twitter_API']['CONSUMER_SECRET']
AUTH_TOKEN = config['Twitter_API']['AUTH_TOKEN']
AUTH_SECRET = config['Twitter_API']['AUTH_SECRET']
