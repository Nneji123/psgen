# psgen
[![Pypi](https://img.shields.io/pypi/v/psgen.svg)](https://pypi.org/project/psgen/0.0.1/)
[![publish-pypi](https://github.com/Nneji123/psgen/actions/workflows/publish.yml/badge.svg)](https://github.com/Nneji123/psgen/actions/workflows/publish.yml)
[![tests](https://github.com/Nneji123/psgen/actions/workflows/test.yml/badge.svg)](https://github.com/Nneji123/psgen/actions/workflows/test.yml)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/Nneji123/psgen/dev/LICENSE)

## Description

Random password generator made with python.

## Installation & usage

```bash
$> pip3 install psgen

$> psgen
52db9s%NhA1C
```

## Install from source
```
git clone https://github.com/Nneji123/psgen.git
cd psgen
pip install -e .
```

## Use within another Python script

```python
>>> from src.psgen import generate_password

>>> generate_password(12) # this will print out a 12 character password
'52db9s%NhA1C'
```

## Advanced options

```
$ psgen -h
usage: psgen [-h] [--number NUMBER]

Generate a random password with numbers, symbols and letters.

optional arguments:
  -h, --help       show this help message and exit
  --number NUMBER  Write the length of the password you want to generate.The default value is 12. Example psgen --number 12

Happy password creating! :)
```
