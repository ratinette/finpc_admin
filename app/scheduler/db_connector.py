from functools import wraps

from django.db import connection


def db_auto_reconnect(func):
    """Auto reconnect db when mysql has gone away."""

    @wraps(func)
    def wrapper(*args, **kwagrs):
        try:
            connection.connection.ping()
        except Exception:
            connection.close()
        return func(*args, **kwagrs)

    return wrapper
