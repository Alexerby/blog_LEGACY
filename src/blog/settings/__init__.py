import os
import json


CONFIG_FILE = '/etc/blog/config.json'

with open(CONFIG_FILE) as f:
    config = json.load(f)
    if config['PROD']:
        from .prod import *
    else:
        from .dev import *

SECRET_KEY = config['SECRET_KEY']
