from .util import ensure_type

class PriceData(object):
    def __init__(self,
                 symbol,
                 price,
                 timestamp,
                 ):
        self.symbol = symbol
        self.price = float(price)
        self.timestamp = int(timestamp)

        ensure_type(symbol, basestring)
        ensure_type(timestamp, int)
