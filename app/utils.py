import random
import string


def randomword(length=10):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
