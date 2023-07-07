class Validate:
    error = None

    def valid(self) -> None:
        def _filter(arg: str):
            return all((
                not arg.startswith('__'),
                not arg.endswith('__'),
                callable(getattr(self, arg)),
                arg != 'valid', # To avoid recursive calls.
            ))

        for method in filter(_filter, dir(self)):
            getattr(self, method)()
