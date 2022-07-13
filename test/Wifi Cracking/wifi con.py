#import hashlib
from pbkdf2 import PBKDF2
ssid = 'cyberpunk' 
password = 'uwu'

print("Pairwise Master Key (PMK): " + PBKDF2(phrase, ssid, 4096).read(32).encode("hex"))