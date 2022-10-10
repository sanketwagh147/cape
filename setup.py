import os
import re

import setuptools

with open(os.path.join(os.path.dirname(__file__), "ffn", "cape/__init__.py"), "r") as fp:
    version = re.search(
        "^__version__ = \\((\\d+), (\\d+), (\\d+)\\)$", fp.read(), re.MULTILINE
    ).groups()


with open(os.path.join(os.path.dirname(__file__), "README.rst"), "r") as fp:
    description = fp.read().replace("\r\n", "\n")

setuptools.setup(
    name="cape",
    version=".".join(version),
    author="Nathan Ramos, CFA©",
    author_email="info@nrcapitalmanagement.com",
    description="Financial application for Python",
    keywords="python finance quant valuation",
    url="https://github.com/nathanramoscfa/cape",
    license="MIT",
    packages=["cape", "cape/cape"],
    long_description=description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
    ],
)
