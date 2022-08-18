# Getting Started
To use `psgen` you have to do the following.
 Make sure you have python3 and pip installed. Then install psgen:
```console
$ pip install psgen
or
$ pip3 install psgen
or install directly from source
$ git clone https://github.com/Nneji123/psgen.git
$ cd psgen
$ pip install -e .
```

## How to use psgen
`psgen` comes with a CLI tool and is also a python package meaning you can use it from the terminal or in a python script.

### How to use the CLI tool:

```console
$ psgen
5?1T~0Xd*m>G
```
`psgen`  will create and print out a 12 character password containing uppercase, lowercase, digits and symbols by default.

### CLI Commands
  To get the CLI commands run `psgen --help` or `psgen -h`
```console
$ psgen --help
usage: psgen [-h] [--number NUMBER] [--nodigit NODIGIT] [--noupcase NOUPCASE] [--nolowercase NOLOWERCASE] [--nosymbols NOSYMBOLS]
             [--onlydigits ONLYDIGITS] [--onlylocase ONLYLOCASE] [--onlyupcase ONLYUPCASE] [--onlysymbols ONLYSYMBOLS]

Generate a random password with numbers, symbols and letters.

optional arguments:
  -h, --help            show this help message and exit
  
  --number NUMBER       
  
  Write the length of the password you want to generate.The default value is 12. Example psgen --number 12
  
  
  --nodigit NODIGIT     
  
  This will generate a random password with no digits. Example psgen --nodigit 12
  
  
  --noupcase NOUPCASE   
  
  This will generate a random password with no uppercase letters. Example psgen --noupcase 12
  
  
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
```

### How to use psgen in a python script
To use psgen in your python script, you have to import it.
- #### Example
```Python
from psgen.psgen import generate_password_all

print(generate_password_all(12))
```
The above code will generate and print out a 12 character password containing letters, symbols and numbers.