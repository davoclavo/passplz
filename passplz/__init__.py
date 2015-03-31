"""A simple password generator"""

from pkg_resources import get_distribution, DistributionNotFound
import os.path
from uuid import uuid4

try:
    _dist = get_distribution('passplz')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'passplz')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version


def generate_password(password_length=16):
    """Generate a random password of length ``password_length``."""
    random_string = ""
    while len(random_string) < password_length + 4*(password_length/16.0):
        random_string += str(uuid4())
    random_password = random_string.replace('-', '')[:password_length]
    return random_password
