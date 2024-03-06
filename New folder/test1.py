import re
import re

TOKEN_TYPES = [
    ('IF', r'\bif\b'),
    ('ELSE', r'\belse\b'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('NUMBER', r'\d+'),
    ('EQUAL', r'=='),
    ('ASSIGN', r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('QUESTION', r'\?'),
    ('COLON', r':'),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]

def lexer(code):
    tokens = []
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                value = match.group(0)
                if token_type != 'SKIP' and token_type != 'NEWLINE':  # Skip whitespace and newlines
                    tokens.append((token_type, value))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[pos]}")
    return tokens
class Interpreter:
    def _init_(self):
        self.variables = {}

    def evaluate_expression(self, tokens):
        # Simplified evaluation: return integer or boolean
        if tokens[0][0] == 'NUMBER':
            return int(tokens[0][1])
        elif tokens[0][0] == 'IDENTIFIER':
            var_name = tokens[0][1]
            return self.variables.get(var_name, 0)
        # Add more logic for evaluating complex expressions
        
    

    

    def execute(self, tokens):
        index = 0
        while index < len(tokens):
            token_type, value = tokens[index]

            if token_type == 'IDENTIFIER' and index + 1 < len(tokens) and tokens[index + 1][0] == 'ASSIGN':
                # Variable assignment
                var_name = value
                expr_value = self.evaluate_expression(tokens[index + 2:index + 3])
                self.variables[var_name] = expr_value
                index += 3  # Move past the assignment statement

            elif token_type == 'IF':
                condition = self.evaluate_expression(tokens[index + 1:index + 2])
                if condition:
                    # Execute true branch, skipping the condition evaluation
                    index += 2
                    while tokens[index][0] not in ['ELSE', 'NEWLINE']:
                        self.execute([tokens[index]])
                        index += 1
                    # Skip else branch
                    while index < len(tokens) and tokens[index][0] != 'NEWLINE':
                        index += 1
                else:
                    # Skip true branch
                    index += 2
                    while index < len(tokens) and tokens[index][0] not in ['ELSE', 'NEWLINE']:
                        index += 1
                    if tokens[index][0] == 'ELSE':
                        index += 1
                        while index < len(tokens) and tokens[index][0] != 'NEWLINE':
                            self.execute([tokens[index]])
                            index += 1
            else:
                index += 1

    def run(self, code):
        tokens = lexer(code)
        self.execute(tokens)
        print("Execution finished. Variables:", self.variables)

# Sample code in Hansat language
hansat_code = """
x = 5
if x == 5
    y = 10
else
    y = 20
"""

interpreter = Interpreter()
interpreter.run(hansat_code)