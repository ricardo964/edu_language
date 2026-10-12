from token_type import TokenType

token_patterns = [
    (TokenType.NUMBER, r"\d+(\.\d+)?"),
    (TokenType.STRING, r'"[^"\n]*"|\'[^\'\n]*\''),

    (TokenType.ADD, r"\+"),
    (TokenType.SUB, r"-"),
    (TokenType.POW, r"\*\*"),
    (TokenType.MUL, r"\*"),
    (TokenType.DIV, r"/"),
    (TokenType.NOT, r"~"),
    (TokenType.AND, r"&"),
    (TokenType.OR, r"\|"),
    (TokenType.EQUAL, r"=="),
    (TokenType.ASSIGN, r"="),
    (TokenType.LPAREN, r"\("),
    (TokenType.RPAREN, r"\)"),
    (TokenType.LBRACKET, r"\["),
    (TokenType.RBRACKET, r"\]"),
    (TokenType.SEMICOLON, r";"),

    (TokenType.IDENTIFIER, r"[A-Za-z_][A-Za-z0-9_]*"),

    (TokenType.NEWLINE, r"\n"),
    (TokenType.IGNORE, r"[ \t\r]+"),
    (TokenType.UNKNOWN, r"."),
]

keyword_map = {
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "function": TokenType.FUNCTION,
    "loop": TokenType.LOOP,
    "break": TokenType.BREAK,
    "continue": TokenType.CONTINUE,
    "true": TokenType.BOOLEAN,
    "false": TokenType.BOOLEAN,
}
