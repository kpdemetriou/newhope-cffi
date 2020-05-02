from ._cpa import ffi as __ffi, lib as __lib
from .core import generate_keypair_factory, encrypt_factory, decrypt_factory
from .params import *

generate_keypair = generate_keypair_factory(__ffi, __lib, NEWHOPE_CPAKEM_PUBLICKEYBYTES, NEWHOPE_CPAKEM_SECRETKEYBYTES)

encrypt = encrypt_factory(
    __ffi, __lib, NEWHOPE_CPAKEM_PUBLICKEYBYTES, NEWHOPE_CPAKEM_CIPHERTEXTBYTES, NEWHOPE_CPAKEM_PLAINTEXTBYTES
)

decrypt = decrypt_factory(
    __ffi, __lib, NEWHOPE_CPAKEM_SECRETKEYBYTES, NEWHOPE_CPAKEM_CIPHERTEXTBYTES, NEWHOPE_CPAKEM_PLAINTEXTBYTES
)
