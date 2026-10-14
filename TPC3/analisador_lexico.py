import re, sys

SPEC = [
    ('COMMENT', r'\#.*'),
    ('VAR', r'\?\w+'),
    ('LANGUAGE', r'@\w{2}'),
    ('STRING', r'"[^"]*"'),
    ('NUMBER', r'\d+(?:\.\d+)?(?![\w:])'),
    ('CONCEPT', r'[\w:]+'),
    ('SKIP', r'\s+'),
    ('L_DELIMITER', r'{'),
    ('R_DELIMITER', r'}'),
    ('DOT', r'\.'),
    ('ERROR', r'.'),
]

RESERVED = {'LIMIT'}

IGNORED = {'COMMENT', 'SKIP'}

MASTER = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in SPEC))

def tokenize(raw):
    tokens = []
    for m in MASTER.finditer(raw):
        kind = m.lastgroup
        value = m.group()
        if kind in IGNORED:
            continue
        if kind == 'CONCEPT' and value in RESERVED:
            kind = 'RESERVED'
        tokens.append((kind, value))
    return tokens

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    for tok in tokenize(text):
        print(tok)

if __name__ == '__main__':
    main()
