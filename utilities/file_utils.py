from collections.abc import Callable
from utilities.utils import bytes_to_binary

def decodeFromFile(path:str, key:str, decode_function:Callable[[str,str],str])->str:
    """
        Returns a string of ones and zeros
    """
    with open(path) as f:
        bases = f.read()
        try:
            raw_decode_binary = decode_function(bases, key)
        except Exception:
            raise Exception("Decode failed, is your file in the correct format?")
        return raw_decode_binary


def encodeFromFile(path:str, key:str, encode_function:Callable[[str,str],str])->str:
    """
        Returns a string of bases.
    """
    with open(path,"rb") as f:
        bytes = f.read()
        try:
            bases = encode_function(bytes_to_binary(bytes), key)
        except Exception:
            raise Exception("Decode failed, is your file in the correct format?")
        return bases

def saveToFile(path:str, data):
    if(type(data) == str):
        with open(path,"w") as f:
            f.write(data)
    elif(type(data) == bytes):
        with open(path,"wb") as f:
            f.write(data)
    else:
        with open(path,"w") as f:
            f.write(str(data))