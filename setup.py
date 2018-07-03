from setuptools import setup, find_packages

setup(
    name="mystr",
    version="0.1.0",
    packages=find_packages(),
    setup_requires=["cffi>=1.0.0"],
    # install_requires=["cffi>=1.0.0"],
    cffi_modules=["build.py:ffi"],
    test_suite="tests",
)
