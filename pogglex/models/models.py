""" Models for the lexer"""
from typing import Any, Dict, List
import re
import copy

from ply.lex import Lexer

from pogglex.abstracts import LexerProtocol


class PoggLexer(LexerProtocol):
    def __init__(self):
        self.master_re_exp: Any = None  # Master regular expression. This is a list of tuples (re, findex) where re is a compiled
        self.curret_re_exp: Any = None
        self.lex_state_re: Dict = {}
        self.lex_state_re_text: Dict = {}
        self.lex_state_re_names: Dict = {}
        self.lex_state: str = "INITIAL"
        self.lex_state_stack: List = []
        self.lex_state_info: Any = (
            None  # State information
        )
        self.lex_state_ignore: Dict = (
            {}
        )  # Dictionary of ignored characters for each state
        self.lex_state_error_funcs: Dict = (
            {}
        )  # Dictionary of error functions for each state
        self.lex_state_eof_funcs: Dict = (
            {}
        )  # Dictionary of eof functions for each state
        self.lex_re_flags: Dict = (
            0  # Optional re compile flags
        )
        self.lex_data: Dict = (
            None  # Actual input data (as a string)
        )
        self.lex_pos: Dict = (
            0  # Current position in input text
        )
        self.lex_len: Dict = (
            0  # Length of the input text
        )
        self.lex_error_rules: Any = (
            None  # Error rule (if any)
        )
        self.lex_eof_rules: Any = (
            Any  # EOF rule (if any)
        )
        self.lex_tokens: List = (
            None  # List of valid tokens
        )
        self.lex_ignore: str = (
            ""  # Ignored characters
        )
        self.lex_literals: str = ""  # Literal characters that can be passed through
        self.lex_module = None  # Module
        self.line_no: int = 1  # Current line number
        self.lex_optimize: bool = (
            False  # Optimized mode
        )
    
    def __copy__(self, object: Any = None):
        # print the type of object
        print(f"__copy__ called on {object}")
        c = copy.copy(self)

        # if object paramater is supplied then rebind all methods in
        # lex_master_re_exp and lex_state_error_funcs to the object
        if object:
            return re_bind_lexer_methods(
                cls=self,
                _copy=c,

            )
    def input(self, _buffer: str):
        """
        Input new string data.
        """
        if not  isinstance(_buffer[:1], str):
            raise TypeError("Input must be a string")
        self.lex_data = _buffer
        self.lex_pos = 0
        self.lex_len = len(_buffer)
    
    def begin(self, state):
        """
        Set the lexer state
        """
        if state not in self.lex_state_re:
            raise ValueError("Undefined state")
        self.master_re_exp = self.lex_state_re[state]
        self.lex_re_text = self.lex_state_re_text[state]
        self.lex_ignore = self.lex_state_ignore.get(state, "")
        self.lex_error_func_rules = self.lex_state_error_funcs.get(state, None)
        self.lex_eof_func_rules = self.lex_state_eof_funcs.get(state, None)
        self.lex_state = state
    
    def push_state(self, state):
        """
        Push the current state onto the state stack
        """
        self.lex_state_stack.append(self.lex_state)
        self.begin(state)
    
    def pop_state(self):
        """
        Pop the last state off the state stack
        Restores previous state
        """
        self.begin(self.lex_state_stack.pop())
    
    def current_state(self):
        """
        Return the current lexer state
        """
        return self.lex_state
    
    def skip(self, n: int):
        """
        Skip ahead n characters in the input stream
        """
        self.lex_pos += n
    
    def token(self):
        """
        Return the next token from the Lexer
        """
        _lex_pos = self.lex_pos
        _lex_data = self.lex_data
        _lex_len = self.lex_len
        _lex_ignore = self.lex_ignore

        while (_lex_pos < _lex_len):
            if _lex_data[_lex_pos] in _lex_ignore:
                _lex_pos += 1
                continue
            
            # Look for regex match
            self.find_regex_match(

            )
    def find_regex_match(self: LexerProtocol):
        pass

    



def re_bind_lexer_methods(cls: Lexer, _copy: Lexer):
    new_tab = {}
    for key, r_item in cls.master_re_exp.items():
        new_re = []
        for current_re, f_index in r_item:
            new_f_index = []
            for f in f_index:
                if not f or not f[0]:
                    new_f_index.append(f)
                new_f_index.append(
                    (
                        getattr(
                            object, f[0].__name__,f[1]
                        )
                    )
                )
            new_re.append((current_re, new_f_index))
        new_tab[key] = new_re
    _copy.master_re_exp = new_tab
    new_tab = {}
    _copy.lex_state_error_funcs = {
        key: getattr(object, f.__name__, f)
        for key, f in cls.lex_state_error_funcs.items()
    }
    _copy.lex_module = object
    return _copy


