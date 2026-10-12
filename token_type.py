from enum import Enum, auto
from dataclasses import dataclass

class TokenType(Enum):
    # id
    IDENTIFIER = auto()

    # literal
    NUMBER = auto()
    BOOLEAN = auto()
    STRING = auto()

    # operator
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    POW = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    ASSIGN = auto()
    EQUAL = auto()

    # keyword
    IF = auto()
    ELSE = auto()
    FUNCTION = auto()
    LOOP = auto()
    BREAK = auto()
    CONTINUE = auto()

    # other
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    NEWLINE = auto()
    IGNORE = auto()
    UNKNOWN = auto()
    EOF = auto()


@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    line: int
    col: int
