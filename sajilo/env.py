import os
from timeit import default_timer
import sajilo
import sajilo.ast as ast
import sajilo.symbol_table
import math
import random
import sys


def substr(s: str, start: int, length: int):
    return s[start:start + length]


def str_pos(sub: str, string: str):
    return string.index(sub)


def str_format(string, *args):
    return string % tuple(args)


def array_push(arr: list, value):
    arr.append(value)


def array_pop(arr: list):
    return arr.pop()


def array_insert(arr: list, i: int, x):
    arr.insert(i, x)


def array_remove(arr: list, i: int):
    return arr.pop(i)


def array_reverse(arr: list):
    arr.reverse()


def array_sort(arr: list):
    arr.sort()

def file_close(f):
    f.close()

def file_write(f, data):
    f.write(data)

def file_read(f, size = None):
    return f.read(size)

def file_seek(f, offset):
    return f.seek(offset)

def file_pos(f):
    return f.tell()

def file_exists(f):
    return os.path.isfile(f)


def declare_env(s: sajilo.symbol_table.SymbolTable):

    f = ast.BuiltInFunction

    # SET OF CONSTANTS
    s.set_sym('pi', math.pi)
    s.set_sym('e', math.e)


    # global variables for the file access.
    s.set_sym('argv', sys.argv)



    s.set_func('anka', f(int))
    s.set_func('dash', f(float))
    s.set_func('sabda', f(str))

    s.set_func('abs', f(abs))
    s.set_func('log', f(math.log))
    s.set_func('log2', f(math.log))


    s.set_func('sin', f(math.sin))
    s.set_func('cos', f(math.cos))
    s.set_func('tan', f(math.tan))
    s.set_func('atan', f(math.atan))

    # string functions
    '''
    String functions are implmented as wrappers around the existing
    String functions from the python library.
    '''
    s.set_func('sanosabda', f(substr))
    s.set_func('lambai', f(len))
    s.set_func('sthan', f(str_pos))
    s.set_func('mathillo', f(str.upper))
    s.set_func('tallo', f(str.lower))
    s.set_func('badala', f(str.replace))
    s.set_func('milau', f(str_format))




    s.set_func('samaya', f(default_timer))

    # Lists are implemented as
    s.set_func('samuha_rakha', f(array_insert))
    s.set_func('samuha_nikala', f(array_pop))
    s.set_func('samuha_pathau', f(array_push))
    s.set_func('samuha_hatau', f(array_remove))
    s.set_func('samuha_reverse', f(array_reverse))
    s.set_func('samuha_krama', f(array_sort))

    # file
    s.set_func('file_khola', f(open))
    s.set_func('file_banda', f(file_close))
    s.set_func('file_lekha', f(file_write))
    s.set_func('file_padha', f(file_read))
    s.set_func('file_khoja', f(file_seek))
    s.set_func('file_sthan', f(file_pos))
    s.set_func('file_chha', f(file_exists))

    # Input from the console is also wrapped around input method
    # Typecasting is required when taking input
    s.set_func('padha', f(input))


def declare_repl(s: sajilo.symbol_table.SymbolTable):
    f = ast.BuiltInFunction

    # SET OF CONSTANTS
    s.set_sym('pi', math.pi)
    s.set_sym('e', math.e)

    # global variables for the file access.
    s.set_sym('argv', sys.argv)

    s.shell_scope_func('anka', f(int))
    s.shell_scope_func('dash', f(float))
    s.shell_scope_func('sabda', f(str))

    s.shell_scope_func('abs', f(abs))
    s.shell_scope_func('log', f(math.log))
    s.shell_scope_func('log2', f(math.log))

    s.shell_scope_func('sin', f(math.sin))
    s.shell_scope_func('cos', f(math.cos))
    s.shell_scope_func('tan', f(math.tan))
    s.shell_scope_func('atan', f(math.atan))

    # string functions
    '''
    String functions are implmented as wrappers around the existing
    String functions from the python library.
    '''
    s.shell_scope_func('sanosabda', f(substr))
    s.shell_scope_func('lambai', f(len))
    s.shell_scope_func('sthan', f(str_pos))
    s.shell_scope_func('mathillo', f(str.upper))
    s.shell_scope_func('tallo', f(str.lower))
    s.shell_scope_func('badala', f(str.replace))
    s.shell_scope_func('milau', f(str_format))

    s.shell_scope_func('samaya', f(default_timer))

    # Lists are implemented as
    s.shell_scope_func('samuha_rakha', f(array_insert))
    s.shell_scope_func('samuha_nikala', f(array_pop))
    s.shell_scope_func('samuha_pathau', f(array_push))
    s.shell_scope_func('samuha_hatau', f(array_remove))
    s.shell_scope_func('samuha_reverse', f(array_reverse))
    s.shell_scope_func('samuha_krama', f(array_sort))

    # file
    s.shell_scope_func('file_khola', f(open))
    s.shell_scope_func('file_banda', f(file_close))
    s.shell_scope_func('file_lekha', f(file_write))
    s.shell_scope_func('file_padha', f(file_read))
    s.shell_scope_func('file_khoja', f(file_seek))
    s.shell_scope_func('file_sthan', f(file_pos))
    s.shell_scope_func('file_chha', f(file_exists))

    # Input from the console is also wrapped around input method
    # Typecasting is required when taking input
    s.shell_scope_func('padha', f(input))

