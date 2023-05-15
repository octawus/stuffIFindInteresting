import re

def evaluate_rpn(expression):
    stack = []
    for token in expression:
        if token.isnumeric():
            stack.append(float(token))
        elif len(token) > 1 and "-" in token:
            stack.append(float(token.lstrip("-")) * -1)
        else:
            b = stack.pop() 
            a = stack.pop()
            if token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
    solution = stack.pop()
    print("solution: {}".format(solution))
    if solution.is_integer():
        return int(solution)
    else:
        return solution



def calc(expression):
    print("expression: {}".format(expression))
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, "~": 3}
    
    stack = []
    output = []
    negative_parenthesis = 0
    i = 0
    
    tokens = re.findall(r'-?\d+\.?\d*|(?<=\()\(|-?\(|\-|\+|\*|\/|\-|\)|(?<=\d)\-', expression)
    while i < len(tokens):
        if bool(re.match(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)', tokens[i])):
            output.append(tokens[i])
            i += 1
        elif tokens[i] in precedence or tokens[i] == "-(":
            if tokens[i] == "-(" :
                if tokens[i-1] and tokens[i-1].isdigit():
                    stack.append("+")
                output.append('-1')
                stack.append("(")
                negative_parenthesis += 1
                i += 1
            else:
                while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[tokens[i]]:
                    output.append(stack.pop())
                else:
                    stack.append(tokens[i])
                i += 1
        elif tokens[i] == '(':
            stack.append(tokens[i])
            i += 1
        elif tokens[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if negative_parenthesis > 0:
                output.append('*')
                negative_parenthesis -= 1
            if stack and stack[-1] == '(':
                stack.pop()
            i += 1
    while stack:
        output.append(stack.pop())
        i += 1
    return evaluate_rpn(output)