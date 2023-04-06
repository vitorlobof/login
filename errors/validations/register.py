import re
import errors.exceptions as ecp

class Validate:
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

class ValidateName(Validate):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def pattern(self) -> None:
        p = re.compile(r"^(?! )[a-zA-ZÀ-ÿ ]*(?<! )$")
        match = re.match(p, self.name)
        if match is None:
            raise ecp.NameDoesNotMatchPatternError()

class ValidateEmail(Validate):
    def __init__(self, email: str) -> None:
        self.email = email

    def pattern(self) -> None:
        p = re.compile(r'[-._%+\w]+@[-.\w]+\.[a-zA-Z]{2,}')
        match = re.match(p, self.email)

        if match is None:
            raise ecp.EmailDoesNotMatchPatternError()

class ValidatePassword(Validate):
    def __init__(
            self, password: str, confirm: str=None) -> None:
        self.password = password
        self.confirm = confirm
    
    def confirmation(self) -> None:
        if self.confirm is None:
            return None

        if self.password != self.confirm:
            raise ecp.PasswordNotConfirmedError()
    
    def numbers(self) -> None:
        match = re.search(r"[0-9]", self.password)
        if match is None:
            raise ecp.PasswordDoesNotMatchPatternError()
    
    def lowercase_letters(self) -> None:
        match = re.search(r"[a-z]", self.password)
        if match is None:
            raise ecp.PasswordDoesNotMatchPatternError()
    
    def uppercase_letters(self) -> None:
        match = re.search(r"[A-Z]", self.password)
        if match is None:
            raise ecp.PasswordDoesNotMatchPatternError()
    
    def special_characters(self) -> None:
        p = r'[\\/!@#$%^&*(),.?":{}|<>]'
        match = re.search(p, self.password)
        if match is None:
            raise ecp.PasswordDoesNotMatchPatternError()
    
    def check_pattern(self) -> None:
        p = r'[a-zA-Z0-9\\/\!@#\$%^&*(),.?":{}|<>]{8,12}'
        match = re.match(p, self.password)
        if match is None:
            raise ecp.PasswordDoesNotMatchPatternError()
