def generate_keypair_factory(ffi, lib, public_key_size, secret_key_size):
    def generate_keypair():
        public_key_buf = ffi.new("unsigned char [{}]".format(public_key_size))
        secret_key_buf = ffi.new("unsigned char [{}]".format(secret_key_size))

        lib.crypto_kem_keypair(public_key_buf, secret_key_buf)

        public_key = bytes(ffi.buffer(public_key_buf, public_key_size))
        secret_key = bytes(ffi.buffer(secret_key_buf, secret_key_size))

        return public_key, secret_key

    return generate_keypair


def encrypt_factory(ffi, lib, public_key_size, ciphertext_size, plaintext_size):
    def encrypt(public_key):
        if not isinstance(public_key, bytes):
            raise TypeError("'public_key' must be of type 'bytes'")

        if len(public_key) != public_key_size:
            raise ValueError(f"'key' must be of length '{ public_key_size }'")

        ciphertext_buf = ffi.new("unsigned char [{}]".format(ciphertext_size))
        plaintext_buf = ffi.new("unsigned char [{}]".format(plaintext_size))

        lib.crypto_kem_enc(ciphertext_buf, plaintext_buf, public_key)

        ciphertext = bytes(ffi.buffer(ciphertext_buf, ciphertext_size))
        plaintext = bytes(ffi.buffer(plaintext_buf, plaintext_size))

        return ciphertext, plaintext

    return encrypt


def decrypt_factory(ffi, lib, secret_key_size, ciphertext_size, plaintext_size):
    def decrypt(secret_key, ciphertext):
        if not isinstance(secret_key, bytes):
            raise TypeError("'secret_key' must be of type 'bytes'")

        if not isinstance(ciphertext, bytes):
            raise TypeError("'ciphertext' must be of type 'bytes'")

        if len(secret_key) != secret_key_size:
            raise ValueError(f"'secret_key' must be of length '{ secret_key_size }'")

        if len(ciphertext) != ciphertext_size:
            raise ValueError(f"'ciphertext' must be of length '{ ciphertext_size }'")

        plaintext_buf = ffi.new("unsigned char [{}]".format(plaintext_size))
        lib.crypto_kem_dec(plaintext_buf, ciphertext, secret_key)
        return bytes(ffi.buffer(plaintext_buf, plaintext_size))

    return decrypt
