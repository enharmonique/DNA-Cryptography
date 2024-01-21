from collections.abc import Callable
from utils import text_to_binary

def decodeFromFile(path:str, key:str, decode_function:Callable[[str,str],str])->str:
    """
        Returns a string of ones and zeros
    """
    # TODO: update so binary files work as well
    # and error handling too
    with open(path) as f:
        bases = f.read()
        raw_decode_binary = decode_function(bases, key)
        return raw_decode_binary


def encodeFromFile(path:str, key:str, encode_function:Callable[[str,str],str])->str:
    """
        Returns a string of bases.
    """
    # TODO: update so binary files work as well
    # and error handling too
    with open(path,"r") as f:
        text = f.read()
        bases = encode_function(text_to_binary(text), key)
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