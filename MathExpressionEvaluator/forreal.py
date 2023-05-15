import re

def evaluate_rpn(expression):
    print("initial expression : {}".format(expression))
    stack = []
    operation = []
    for token in expression:
        print("evaluating {}".format(token))
        if token.isnumeric():
            stack.append(float(token))
            print("stack : {}".format(stack))
        elif len(token) > 1 and "-" in token:
            stack.append(float(token.lstrip("-")) * -1)
            print("stack : {}".format(stack))
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
            print("stack: {}".format(stack))
    solution = stack.pop()
    print("solution: {}".format(solution))
    if solution.is_integer():
        return int(solution)
    else:
        return solution



def calc(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, "~": 3}
    
    stack = []
    output = []
    negative_parenthesis = 0
    i = 0
    
    #tokens = re.findall(r'\d+\.?\d*|\+|\-|\*|\/|\(|\)', expression)
    tokens = re.findall(r'-?\d+\.?\d*|(?<=\()\(|-?\(|\-|\+|\*|\/|\-|\)|(?<=\d)\-', expression)
    print(tokens)
    while i < len(tokens):
        print(output)
        print("evaluating: {}".format(tokens[i]))
        if bool(re.match(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)', tokens[i])):
            output.append(tokens[i])
            print("Normal output: {}".format(output))
            print("Normal stack: {}".format(stack))
            i += 1
        elif tokens[i] in precedence or tokens[i] == "-(":
            if tokens[i] == "-(" :
                if tokens[i-1] and tokens[i-1].isdigit():
                    stack.append("+")
                output.append('-1')
                stack.append("(")
                negative_parenthesis += 1
                print(output)
                print("third output: {}".format(output))
                print("third stack: {}".format(stack))
                i += 1
            else:
                while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[tokens[i]]:
                    # take top of stack and put into output
                    output.append(stack.pop())
                else:
                    stack.append(tokens[i])
                i += 1
                print("else: {}".format(output))
        elif tokens[i] == '(':
            # If the token is a left parenthesis, push it onto the stack
            stack.append(tokens[i])
            print("( output: {}".format(output))
            print("( stack: {}".format(stack))
            i += 1
        elif tokens[i] == ')':
            print("output: {}".format(output))
            print("stack: {}".format(stack))
            # If the token is a right parenthesis, pop operators from the stack and add them to the output queue
            # until a left parenthesis is encountered
            while stack and stack[-1] != '(':
                print("Moving from stack to output")
                output.append(stack.pop())
            if negative_parenthesis > 0:
                output.append('*')
                negative_parenthesis -= 1
            if stack and stack[-1] == '(':
                stack.pop()
            i += 1
    # Pop any remaining operators from the stack and add them to the output queue
    while stack:
        print("final output: {}".format(output))
        print("final stack: {}".format(stack))
        output.append(stack.pop())
        i += 1
    print("-------------EVALUATING---------------------")
    print(output)
    return evaluate_rpn(output)