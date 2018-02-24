from email.utils import parseaddr
from login.models import User_based as User

class OutOfLengthOfNameExc(Exception):
    def __init__(self):
        Exception.__init__(self,"Public name must have 3..70 length")

class DisallowedSymbolsInUserNameExc(Exception):
    def __init__(self):
        Exception.__init__(self, 
        "Disallowed symbols in iser name\n(alpha and numeric are allowed)")

class DisallowedSymbolsInNameExc(Exception):
    def __init__(self):
        Exception.__init__(self,
        "Public name has disallowed characters\n(only alpha and spaces allowed)")

class ShortLengthOfPasswordExc(Exception):
    def __init__(self):
        Exception.__init__(self,"Password is too short (min. 6..80 characters)")

class NotProperEmailExc(Exception):
    def __init__(self):
        Exception.__init__(self, "Email has not proper format")

class NotUniqueEmailExc(Exception):
    def __init__(self):
        Exception.__init__(self, "Email already registered")

class NotUniqueUsernameExc(Exception):
    def __init__(self):
        Exception.__init__(self, "Username already registered")

class UnknownErrorExc(Exception):
    def __init__(self):
        Exception.__init__(self, "Unknown error")



def check_for_error(user_name='Pidor', public_name='Default', user_email='Default@kek.ru', password='12345678'):
    
    if not (3 <= public_name.__len__() <= 40):
        raise OutOfLengthOfNameExc
    
    for word in public_name.split():
        if word.isalpha() == False:
            raise DisallowedSymbolsInNickExc

    if user_name.isalnum() == False:
        raise DisallowedSymbolsInNameExc
    
    if password.__len__() < 4:
        raise ShortLengthOfPasswordExc
    
    if '@' not in user_email:
        raise NotProperEmailExc

def check_unique_user_name(original_user_name):
    user_name = original_user_name.lower()
    try:
        User.objects.get(user_name = user_name)
    except User.DoesNotExist:
        pass
    except:
        raise UnknownErrorExc
    else:
        raise NotUniqueUsernameExc


def check_unique_user_email(original_user_email):
    user_email = original_user_email.lower()
    try:
        User.objects.get(user_email = user_email)
    except User.DoesNotExist:
        pass
    except:
        raise UnknownErrorExc
    else:
        raise NotUniqueEmailExc

