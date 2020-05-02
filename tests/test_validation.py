import pytest
import newhope.cca
import newhope.cpa


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_encrypt_public_key_type(variant):
    pk, sk = variant.generate_keypair()

    with pytest.raises(TypeError):
        variant.encrypt("0" * len(pk))


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_encrypt_public_key_longer(variant):
    pk, sk = variant.generate_keypair()

    with pytest.raises(ValueError):
        variant.encrypt(pk + b"\0")


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_encrypt_public_key_shorter(variant):
    pk, sk = variant.generate_keypair()

    with pytest.raises(ValueError):
        variant.encrypt(pk[:-1])


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_secret_key_type(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(TypeError):
        variant.decrypt("0" * len(sk), ciphertext)


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_secret_key_type(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(TypeError):
        variant.decrypt(sk, "0" * len(ciphertext))


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_secret_key_longer(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(ValueError):
        variant.decrypt(sk + b"\0", ciphertext)


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_secret_key_shorter(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(ValueError):
        variant.decrypt(sk[:-1], ciphertext)


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_ciphertext_longer(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(ValueError):
        variant.decrypt(sk, ciphertext + b"\0")


@pytest.mark.parametrize("variant", [newhope.cca, newhope.cpa])
def test_decrypt_ciphertext_shorter(variant):
    pk, sk = variant.generate_keypair()
    ciphertext, plaintext = variant.encrypt(pk)

    with pytest.raises(ValueError):
        variant.decrypt(sk, ciphertext[:-1])
