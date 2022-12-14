# psgen
[![Pypi](https://img.shields.io/pypi/v/psgen.svg)](https://pypi.org/project/psgen/)
[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)](https://pypi.org/project/psgen/)
[![Downloads](https://pepy.tech/badge/psgen)](https://pepy.tech/project/psgen)
[![tests](https://github.com/Nneji123/psgen/actions/workflows/test.yml/badge.svg)](https://github.com/Nneji123/psgen/actions/workflows/test.yml)
[![docs](https://github.com/Nneji123/psgen/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/Nneji123/psgen/actions/workflows/publish-docs.yml)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/Nneji123/psgen/dev/LICENSE)

## Description

Random password generator tool made with python.

## Installation & usage

```console   

$ pip install psgen 

$ psgen
52db9s%NhA1C
```



## Install from source


```console
$ git clone https://github.com/Nneji123/psgen.git
$ cd psgen
$ pip install -e .
```



## Use within another Python script


```Python
>>> from psgen.psgen import generate_password_all

>>> generate_password(12) # this will print out a 12 character password
'52db9s%NhA1C'
```

**For more information visit the official [documentation.](https://nneji123.github.io/psgen/)**



## Advanced options


```console
$ psgen --help
usage: psgen [-h] [--number NUMBER] [--nodigit NODIGIT] [--noupcase NOUPCASE] [--nolowercase NOLOWERCASE] [--nosymbols NOSYMBOLS]
             [--onlydigits ONLYDIGITS] [--onlylocase ONLYLOCASE] [--onlyupcase ONLYUPCASE] [--onlysymbols ONLYSYMBOLS]

Generate a random password with numbers, symbols and letters.

optional arguments:
  -h, --help            show this help message and exit
  --number NUMBER       Write the length of the password you want to generate.The default value is 12. Example psgen --number 12
  --nodigit NODIGIT     This will generate a random password with no digits. Example psgen --nodigit 12
  --noupcase NOUPCASE   This will generate a random password with no uppercase letters. Example psgen --noupcase 12
  --nolowercase NOLOWERCASE
                        This will generate a random password with no lowercase letters. Example psgen --nolowercase 12
  --nosymbols NOSYMBOLS
                        This will generate a random password with no symbols. Example psgen --nosymbols 12
  --onlydigits ONLYDIGITS
                        This will generate a random password with only digits. Example psgen --onlydigits 12
  --onlylocase ONLYLOCASE
                        This will generate a random password with only lowercase letters. Example psgen --onlylocase 12
  --onlyupcase ONLYUPCASE
                        This will generate a random password with only uppercase letters. Example psgen --onlyupcase 12
  --onlysymbols ONLYSYMBOLS
                        This will generate a random password with only symbols. Example psgen --onlysymbols 12

Happy password creating! :)
```



## License
[MIT](https://github.com/Nneji123/psgen/dev/LICENSE)
