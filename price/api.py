
from .backends import quandl
from .util import ensure_type


CONST_TO_BACKEND = {
    1: quandl,
}


def get(symbol, backend_const, allow_cached=True):
    """
    Get price information for a certain symbol.

    """
    ensure_type(symbol, basestring)
    ensure_type(backend_const, int)

    backend = CONST_TO_BACKEND.get(backend_const)

    if not backend:
        raise ValueError("backend doesn't exist for const %r" % backend_const)

    return backend.get(symbol, allow_cached=allow_cached)
