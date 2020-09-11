import time
import sajilo.parser as p
import sajilo.ast
import sajilo.env
import sajilo.exceptions
import pprint
import sys


# One pass compiler execution
def execute(source, show_ast: bool=False, disable_warnings: bool=True):
    p.disable_warnings = disable_warnings

    try:
        res = p.get_parser().parse(source)
        sajilo.env.declare_env(sajilo.ast.symbols)

        for node in res.children:
            node.eval()
        
        # If show AST command is given, show the AST
        if show_ast:
            print("\n\n" + '=' * 80, ' == Syntax tree ==')

            pp = pprint.PrettyPrinter()
            pp.pprint(res.children)
            pp.pprint(sajilo.ast.symbols.table())
        

    except Exception as e:
        print(e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
        if not disable_warnings:
            raise e

# Interpreter like execution
def shell(source):
    try:
        res = p.get_parser().parse(source)
        sajilo.env.declare_repl(sajilo.ast.symbols)

        for node in res.children:
            node.eval()

        # If show AST command is given, show the AST

    except Exception as e:
        print(e.__class__.__name__ + ': ' + str(e), file=sys.stderr)
