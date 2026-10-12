import re
from token_type import TokenType, Token
from patterns import token_patterns, keyword_map

class Lexer:
    REGEX = re.compile('|'.join(
        f'(?P<{t.name}>{pattern})'
        for t, pattern in token_patterns
    ))

    @staticmethod
    def tokenize(source: str) -> list[Token]:
        tokens = []
        line = 1
        line_start = 0

        for match in Lexer.REGEX.finditer(source):
            kind = match.lastgroup
            value = match.group()
            col = match.start() - line_start + 1

            if kind == TokenType.NEWLINE.name:
                line += 1
                line_start = match.end()
                continue

            if kind == TokenType.IGNORE.name:
                continue

            if kind == TokenType.UNKNOWN.name:
                raise SyntaxError(f"unknown character {value!r} at {line}:{col}")

            token_type = TokenType[kind]
            
            if token_type == TokenType.IDENTIFIER:
                token_type = keyword_map.get(value, TokenType.IDENTIFIER)

            if token_type not in (TokenType.IDENTIFIER, TokenType.NUMBER, TokenType.BOOLEAN):
                value = None
            
            tokens.append(Token(token_type, value, line, col))

        tokens.append(Token(TokenType.EOF, None, line, len(source) - line_start + 1))
        return tokens
