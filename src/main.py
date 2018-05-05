#!/usr/bin/env python

from src import Lury
import colorama
from termcolor import colored

colorama.init()

code = '''a = [1, 3, 5]
b = [2, 4, 6]
a ~ b''' + '\n'

print(colored('input:', 'green', attrs=['bold']), code, sep='\n')
output = Lury.parse(code)

if output is not None:
    print(colored('output:', 'green', attrs=['bold']), output, sep='\n')

    # '''
    print(colored('result:', 'green', attrs=['bold']), sep='\n')
    from py_mini_racer import py_mini_racer
    ctx = py_mini_racer.MiniRacer()
    result = ctx.eval(output)
    print(result, sep='\n')
    # '''
