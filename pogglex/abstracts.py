""" Abstracts for Pogglex."""
from dataclasses import dataclass
import dataclasses
import re
from typing import Any, Dict, List


@dataclass
class LexDefs:
    """Defiitions for the lexer."""

    module: str = None
    object: str = None
    debug: bool = False
    optimize: bool = False
    lex_tab: str = "lextab"
    re_flags = int(re.VERBOSE)
    nowarn: bool = False
    output_dir: str = None
    debug_log: str = None
    error_log = Any = None

@dataclass
class LexerProtocol:
    master_re_exp: Any = None  # Master regular expression. This is a list of tuples (re, findex) where re is a compiled
    curret_re_exp: Any = None
    lex_state_re: Dict = {}
    lex_state_re_text: Dict = {}
    lex_state_re_names: Dict = {}
    lex_state: str = "INITIAL"
    lex_state_stack: List = []
    lex_state_info: Any = (
        None  # State information
    )
    lex_state_ignore: Dict = (
        {}
    )  # Dictionary of ignored characters for each state
    lex_state_error_funcs: Dict = (
        {}
    )  # Dictionary of error functions for each state
    lex_state_eof_funcs: Dict = (
        {}
    )  # Dictionary of eof functions for each state
    lex_re_flags: Dict = (
        0  # Optional re compile flags
    )
    lex_data: Dict = (
        None  # Actual input data (as a string)
    )
    lex_pos: Dict = (
        0  # Current position in input text
    )
    lex_len: Dict = (
        0  # Length of the input text
    )
    lex_error_rules: Any = (
        None  # Error rule (if any)
    )
    lex_eof_rules: Any = (
        Any  # EOF rule (if any)
    )
    lex_tokens: List = (
        None  # List of valid tokens
    )
    lex_ignore: str = (
        ""  # Ignored characters
    )
    lex_literals: str = ""  # Literal characters that can be passed through
    lex_module = None  # Module
    line_no: int = 1  # Current line number
    lex_optimize: bool = (
        False  # Optimized mode
    )
