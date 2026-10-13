import re, sys

SPEC = [
    ('COMMENT', r'\#.*'),
    ('VAR', r'\?\w+'),
    ('LANGUAGE', r'@\w{2}'),
    ('STRING', r'"[^"]*"'),
    ('CONCEPT', r'[\w:]+')
]

def tokenize(raw, spec):
    tokens = []

    for pair in spec:
        matches = re.findall(pair[1], raw)
        for match in matches:
            tokens.append((pair[0], match))
    return tokens

def main():
    if len(sys.argv) < 2:
        print('expecting an argument as the raw text to tokenize')
        return
    print(tokenize(sys.argv[1], SPEC))

if __name__ == '__main__':
    main()

