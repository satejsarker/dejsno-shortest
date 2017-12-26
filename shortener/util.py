from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase +string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(Instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=SHORTCODE_MIN)
    Klass=Instance.__class__
    qs_exists=Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=SHORTCODE_MIN)
    
