import os
import logging

from .util import ensure_type

logging.basicConfig()


class Config(object):
    quandl_api_key = os.environ.get('QUANDL_API_KEY')
    quandl_api_url = os.environ.get(
        'QUANDL_API_URL', 'https://www.quandl.com/api/v3')

    # How long do we cache prices for? Quandl only updates daily...
    quandl_cache_time_secs = int(os.environ.get(
        'QUANDL_CACHE_TIME_SECS', 60 * 60))
    # How many items do we hold in the cache?
    quandl_cache_items = 10000

    def validate(self):
        ensure_type(self.quandl_api_key, basestring)


config = Config()
config.validate()
