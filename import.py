import pip

try:
    __import__('imp').find_module('Crypto')
    from Crypto import Random
    from Crypto.Cipher import AES
except ImportError:
    pip.main(['install', 'pycryptodome'])
    from Crypto import Random
    from Crypto.Cipher import AES
    pass
