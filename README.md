# sanic-fire

sanic-fire is an extension for Sanic that adds support for writing external commands to your application.

## install

    $ pip install sanic-fire
    
## quick start

1.Step1: Create manager.py file in your project root directory.

```
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sanic_fire import cmd
from sanic_fire.core import command_class, command_func


@command_class
class Hello(object):
    """ Annonation """
    
    def hello(self, value='world'):
        """ hello """
        return 'hello, ' + str(value)


@command_func
def sync_db():
    return 'init db'


if __name__ == '__main__':
    cmd()
```     
        
2.Step2: Run command on terminal:
```
python3 manager.py sync_db
python3 manager.py Hello hello
```
