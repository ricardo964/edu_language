from lexer import Lexer

def main():
    source = "variable = false;\nxmax = 10 ** 2;"
    tokens = Lexer.tokenize(source)
    print(*tokens, sep="\n")

if __name__ == "__main__":
    main()
