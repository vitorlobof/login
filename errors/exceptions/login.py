class LoginError(Exception):
    """
    Exception raised when an user tries to login and commits a mistake.
    """

class EmailNotFoundError(LoginError):
    """
    Exception raised when email is not found in the database.
    """
    MSG = 'Este email não foi cadastrado.'

class PasswordIncorrectError(LoginError):
    """
    Exception raised when the password is incorrect.
    """
    MSG = 'Senha incorreta.'

# Errors for when a user tries to use a functionality that
# demands login, without being logged in.
class LoginNeededError(Exception):
    """
    Exception raised when functions that need a login are
    called by an user that is not logged in.
    """
    MSG = 'Para realizar esta ação, é necessário estar logado.'

class LoginToAccessProfileError(LoginNeededError):
    """
    Exception raised when user tries to access the
    profile page without being logged in.
    """
    MSG = 'Para acessar a página de perfil é necessário estar logado.'
