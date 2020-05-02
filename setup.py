from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), "README.rst"), encoding="utf-8") as handle:
    readme = handle.read()

setup(
    name="newhope-cffi",
    version="0.0.2",
    description="Tested, cross-platform Python 3 bindings for the NewHope key exchange mechanism supporting both NewHope1024-CPA-KEM and NewHope1024-CCA-KEM.",
    long_description=readme,
    url="https://github.com/kpdemetriou/newhope-cffi",
    author="Phil Demetriou",
    author_email="inbox@philonas.net",
    license="BSD",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["cffi>=1.4.0"],
    cffi_modules=["build.py:cca_ffi", "build.py:cpa_ffi"],
    install_requires=["cffi>=1.4.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: C",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
    ],
)
