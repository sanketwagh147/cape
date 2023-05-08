from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='cape',
    version='0.0.0',
    packages=['cape'],
    url='https://github.com/nathanramoscfa/nrcapital',
    license='MIT',
    author='Nathan Ramos',
    author_email='nathan.ramos.cfa@gmail.com',
    description='Financial application for the evaluation of equity and bond exchange-traded funds (ETFs) and common '
                'stocks. ',
    python_requires='>=3.8, <3.11',
    install_requires=['pandas', 'ipython', 'setuptools', 'django', 'tqdm'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
)
