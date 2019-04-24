import string
import random


def create_email(chars=string.ascii_uppercase + string.digits):
    thesize = random.randint(12, 22)
    return ''.join(random.choice(chars) for _ in range(thesize))


def create_password(chars=string.ascii_uppercase + string.digits):
    thesize = random.randint(20, 30)
    return ''.join(random.choice(chars) for _ in range(thesize))



