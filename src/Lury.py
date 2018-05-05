#!/usr/bin/env python

from io import StringIO
from typing import Optional
from antlr4 import *
from src.LuryLexer import LuryLexer
from src.LuryParser import LuryParser
from src.LuryListener import LuryListener


def parse(code: str) -> Optional[str]:
    input_stream = InputStream(code)
    lexer = LuryLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LuryParser(stream)
    program = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        return None

    string_io = StringIO()
    listener = LuryListener(string_io)
    walker = ParseTreeWalker()
    walker.walk(listener, program)

    return string_io.getvalue()
