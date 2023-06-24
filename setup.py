from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="casino-dice",
    version="1.0.0",
    author="Anthony V. Ozdemir",
    author_email="anthony@anthonyozdemir.com",
    description="A library for generating byte objects from physical casino dice rolls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anthony-ozdemir/casino-dice",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
    ],
    python_requires='>=3.7',
    install_requires=[],
)
