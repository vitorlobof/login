class RegisterError(Exception):
    """
    Exception raised for register validation errors.
    """

# Errors related to name.
class NameDoesNotMatchPatternError(RegisterError):
    """
    Exception raised when a name does not match the pattern
    expected for a name.
    """
    MSG = 'Nome deve conter apenas letras e espaços, e, não pode começar ou terminar com espaços.'

# Errors related to email.
class EmailDoesNotMatchPatternError(RegisterError):
    """
    Exception raised when a email does not match the pattern
    expected for a email.
    """
    MSG = 'Email deve ter o formato "apenas_um_exemplo@exem.algo".'

class EmailAlreadyRegisteredError(RegisterError):
    """
    Exception raised when user tries to register an
    email that is already registed.
    """
    MSG = 'Email já registrado, tente fazer login.'

# Errors related to password.
class PasswordDoesNotMatchPatternError(RegisterError):
    """
    Exception raised when a password does not match the pattern
    expected for a password.
    """
    MSG = 'Senha deve conter caracteres especiais, letras e números.'

class PasswordNotConfirmedError(RegisterError):
    """
    Exception raised when the password and the confirmation do
    not match.
    """
    MSG = 'A senha e a confirmação da senha devem ser iguais.'

