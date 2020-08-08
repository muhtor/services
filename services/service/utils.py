from .models import Profile
import secrets


class GetCurrentLanguage(object):
    @staticmethod
    def get_language(header=None, user=None):
        if user.is_anonymous:
            if 'Accept-Language' in header:
                lang = header['Accept-Language'][:2]
            else:
                lang = 'en'
            return lang
        else:
            try:
                lang = Profile.objects.get(user=user).language[:2]
            except Profile.DoesNotExist:
                if 'Accept-Language' in header:
                    lang = header['Accept-Language'][:2]
                else:
                    lang = 'en'
            return lang


def print_ln(txt=None, t=None):
    if txt and t is not None:
        return print("-->", txt, "<--", type(t))
    elif txt != "":
        return print(txt)
    else:
        return print()


def get_random_string():
    length = 20
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    allowed_number = '0123456789'
    """
    Return a securely generated random string.
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


