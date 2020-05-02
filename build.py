import platform
from cffi import FFI
from pathlib import Path

newhope_root_path = Path(__file__).parent
newhope_sources_path = newhope_root_path / "sources"

newhope_definitions = """
    int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
    int crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
    int crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);
"""


def prepare_variant(module, variant):
    header_path = (newhope_sources_path / f"{variant}.h").resolve()
    extra_kwargs = {}

    ffi = FFI()
    ffi.cdef(newhope_definitions)

    sources = [
        f"sources/{variant}.c",
        "sources/randombytes.c",
        "sources/cpapke.c",
        "sources/fips202.c",
        "sources/verify.c",
        "sources/poly.c",
        "sources/ntt.c",
        "sources/reduce.c",
        "sources/precomp.c",
    ]

    if "Windows" in platform.system():
        extra_kwargs["extra_link_args"] = ["/NODEFAULTLIB:MSVCRTD"]
        extra_kwargs["libraries"] = ["advapi32"]

    ffi.set_source(
        module, f'#include "{ str(header_path) }"', sources=sources, **extra_kwargs,
    )

    return ffi


cca_ffi = prepare_variant("newhope._cca", "ccakem")
cpa_ffi = prepare_variant("newhope._cpa", "cpakem")

if __name__ == "__main__":
    cca_ffi.compile(verbose=True)
    cpa_ffi.compile(verbose=True)
