
import time

from dateutil.parser import parse


class BackendException(Exception):
    """
    Exception signaling that something bad happened within a backend.

    """

def ensure_type(thing, type_or_types, allow_none=False):
    if not isinstance(type_or_types, tuple):
        type_or_types = (type_or_types,)

    if allow_none:
        type_or_types = type_or_types + (type(None),)

    exp_str = ', '.join(str(t) for t in type_or_types)

    if not isinstance(thing, type_or_types):
        raise ValueError(
            "expected type(s) %r; got %r" % (exp_str, type(thing)))


def date_str_to_timestamp(date_str):
    return int(time.mktime(parse(date_str).timetuple()))
