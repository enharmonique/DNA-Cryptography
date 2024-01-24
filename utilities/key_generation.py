import time
import math
import random
def generate_secure_key():
    random.seed(math.fmod(time.time(),0.1))
    #base64 literals, about 8*3 "real" bytes
    return ''.join(random.choice(list("abcdefghijklmnopqrstuvwxyz0123456789+/"))*32 for _ in range(1000))