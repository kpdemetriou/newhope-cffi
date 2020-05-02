import pytest
import newhope.cca
import newhope.cpa
from secrets import compare_digest


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_keypair(variant):
    pk, sk = variant.generate_keypair()
    assert pk and sk


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_encrypt(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)
    assert ciphertext and plaintext


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_valid(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext_original = variant.encrypt(pk)
    plaintext_recovered = variant.decrypt(sk, ciphertext)

    assert plaintext_recovered
    assert compare_digest(plaintext_original, plaintext_recovered)


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_invalid(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext_original = variant.encrypt(pk)

    ciphertext = bytearray(ciphertext)
    ciphertext[len(ciphertext) // 2] = (ciphertext[len(ciphertext) // 2] + 1) % 256
    ciphertext = bytes(ciphertext)

    plaintext_recovered = variant.decrypt(sk, ciphertext)

    assert plaintext_recovered
    assert not compare_digest(plaintext_original, plaintext_recovered)
