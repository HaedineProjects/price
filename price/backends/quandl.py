"""
Price backend for Quandl (https://www.quandl.com/blog/api-for-stock-data).

"""

import logging

import requests
from expiringdict import ExpiringDict

from price.settings import config
from price.models import PriceData
from price.util import BackendException, date_str_to_timestamp

log = logging.getLogger(__name__)

_CACHE = ExpiringDict(config.quandl_cache_items, config.quandl_cache_time_secs)

def get(symbol, allow_cached=True):
    from_cache = _CACHE.get(symbol)

    if allow_cached and from_cache:
        log.info("Returning price data for %r from cache", symbol)
        return from_cache

    data = get_from_quandl(symbol)
    _CACHE[symbol] = data

    return data


def get_from_quandl(symbol):
    resp = requests.get(
        "%s/datasets/WIKI/%s.csv?api_key=%s" % (
            config.quandl_api_url,
            symbol.upper(),
            config.quandl_api_key,
        )
    )

    if not resp.ok:
        log.error(
            "Unable to retrieve price info for %r (status code %s):\n%s",
            symbol, resp.status_code, resp.content)
        raise BackendException("HTTP request to Quandl failed.")

    try:
        # Format expected is Date,Open,High,Low,Close,...
        most_recent_line = resp.content.split('\n')[1]
        data = most_recent_line.split(',')
        timestamp = date_str_to_timestamp(data[0])
        price = float(data[4])
    except Exception:
        msg = "Quandl response not as expected."
        log.exception(msg)
        raise BackendException(msg)

    return PriceData(symbol, price, timestamp)
