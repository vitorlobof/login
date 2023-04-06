import errors.exceptions as ecp

def _filter(arg):
    to_remove = {
        'LoginError',
        'RegisterError',
    }

    return not any((
        arg.startswith('__'),
        arg.endswith('__'),
        arg in to_remove,
    ))

ERRORS = filter(_filter, dir(ecp.login) + dir(ecp.register))
ERRORS = [getattr(ecp, name) for name in ERRORS]

def msg(id: int) -> str:
    try:
        return ERRORS[int(id)].MSG
    except (IndexError, TypeError, ValueError):
        pass

def idx(error: Exception) -> int:
    try:
        return ERRORS.index(type(error))
    except ValueError:
        pass
