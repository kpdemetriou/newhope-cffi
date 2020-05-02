NewHope CFFI
============

`NewHope <https://newhopecrypto.org/data/NewHope_2019_07_10.pdf>`__ is a
key exchange protocol based on the Ring-Learning-with-Errors (Ring-LWE)
problem and a round 2 candidate submission in the `Post-Quantum
Cryptography
Standardization <https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization>`__
project organised by `NIST <https://www.nist.gov/>`__.

This package provides tested, performant **Python 3** CFFI bindings to
the `NewHope reference
implementation <https://github.com/newhopecrypto/newhope>`__ with minor,
cautious adjustments for cross-platform compatibility.

Installation
============

You can install this package using ``pip`` or the included ``setup.py``
script:

::

   # Using pip
   pip install newhope-cffi

   # Using setup.py
   python setup.py install

Usage
=====

.. code:: python

   from newhope import generate_keypair, encrypt, decrypt
   from secrets import compare_digest

   # Alice generates a public key
   public_key, secret_key = generate_keypair()

   # Bob derives a secret (the plaintext) and encrypts it with Alice's public key to produce a ciphertext
   ciphertext, plaintext_original = encrypt(public_key)

   # Alice decrypts Bob's ciphertext to derive the now shared secret
   plaintext_recovered = decrypt(secret_key, ciphertext)

   # Compare the original and recovered secrets in constant time
   assert compare_digest(plaintext_original, plaintext_recovered)

License
=======

.. code:: text

   BSD 3-Clause License

   Copyright (c) 2018, Phil Demetriou
   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:

   * Redistributions of source code must retain the above copyright notice, this
     list of conditions and the following disclaimer.

   * Redistributions in binary form must reproduce the above copyright notice,
     this list of conditions and the following disclaimer in the documentation
     and/or other materials provided with the distribution.

   * Neither the name of the copyright holder nor the names of its
     contributors may be used to endorse or promote products derived from
     this software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
   FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
