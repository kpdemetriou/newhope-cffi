from ._cca import ffi as __ffi, lib as __lib
from .core import generate_keypair_factory, encrypt_factory, decrypt_factory
from .params import *

generate_keypair = generate_keypair_factory(__ffi, __lib, NEWHOPE_CCAKEM_PUBLICKEYBYTES, NEWHOPE_CCAKEM_SECRETKEYBYTES)

encrypt = encrypt_factory(
    __ffi, __lib, NEWHOPE_CCAKEM_PUBLICKEYBYTES, NEWHOPE_CCAKEM_CIPHERTEXTBYTES, NEWHOPE_CCAKEM_PLAINTEXTBYTES
)

decrypt = decrypt_factory(
    __ffi, __lib, NEWHOPE_CCAKEM_SECRETKEYBYTES, NEWHOPE_CCAKEM_CIPHERTEXTBYTES, NEWHOPE_CCAKEM_PLAINTEXTBYTES
)
