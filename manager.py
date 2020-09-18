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




