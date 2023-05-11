import re

#def do_sign_stuff(expression):
#    pass 
#
#def to_reverse_polish_notation(expression):
#    output = []
#    operator = []
#    for element in expression:
#        if isnumerical(element):
#            print("Add token {} to output".format(element))
#            output.append(element)
#        elif(element == "+" or element == "-"):
#            operator.append()
#        elif(element == "/" or element == "*")
#            if(operator.head())
#            
#            
#            
#    return rpn_expression

def evaluate_rpn(expression):
    print("initial expresion : {}".format(expression))
    stack = []
    for token in expression:
        print("evaluating {}".format(token))
        if token.isnumeric():
            stack.append(float(token))
            print("stack : {}".format(stack))
        elif len(token) > 1 and "-" in token:
            stack.append(float(token.lstrip("-")) * -1)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
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
    evaluating_parenthesis = False
    i = 0
    
    expression = expression.replace(" ", "")
    #tokens = re.findall(r'\d+\.?\d*|\+|\-|\*|\/|\(|\)', expression)
    tokens = re.findall(r'\d+\.?\d*|(?<=\()\-|\(|\+|\*|\/|\-|\)|(?<=\d)\-', expression)
    #print(tokens)
    while i < len(tokens):
        #print(output)
        #print("evaluating: {}".format(tokens[i]))
        if tokens[i].isdigit():
            output.append(tokens[i])
            #print("Normal output: {}".format(output))
            #print("Normal stack: {}".format(stack))
            i += 1
        elif tokens[i] in precedence:
            if tokens[i] == "-":
                if tokens[i+1].isdigit() and (i == 0 or not tokens[i-1].isdigit()):
                    output.append(tokens[i+1])
                    output.append('-1')
                    output.append('*')
                    i += 2
                    #print("first output: {}".format(output))
                    #print("first stack: {}".format(stack))
                elif tokens[i+1].isdigit() and tokens[i-1].isdigit():
                    output.append('-{}'.format(tokens[i+1]))
                    stack.append('+')
                    i += 2
                    #print("second output: {}".format(output))
                    #print("second stack: {}".format(stack))
                elif tokens[i+1] == '(' and (i == 0 or not tokens[i-1].isdigit()):
                    output.append('-1')
                    evaluating_parenthesis = True
                    #print(output)
                    #print("third output: {}".format(output))
                    #print("third stack: {}".format(stack))
                    i += 1
                else:
                    while stack and stack[-1] in precedence and precedence[stack[-1]] > precedence[tokens[i]]:
                        # take top of stack and put into output
                        output.append(stack.pop())
                    stack.append(tokens[i])
                    i += 1
                    #print("last output: {}".format(output))
                    #print("last stack: {}".format(stack))
            else:
            # While stack is not empty, and last element of stack is in precedence and last
            # element of stack has higher precedence than the current evaluated token
                while stack and stack[-1] in precedence and precedence[stack[-1]] > precedence[tokens[i]]:
                    # take top of stack and put into output
                    output.append(stack.pop())
                stack.append(tokens[i])
                i += 1
                #print("else: {}".format(output))
        elif tokens[i] == '(':
            # If the token is a left parenthesis, push it onto the stack
            stack.append(tokens[i])
            #print("( output: {}".format(output))
            #print("( stack: {}".format(stack))
            i += 1
        elif tokens[i] == ')':
            # If the token is a right parenthesis, pop operators from the stack and add them to the output queue
            # until a left parenthesis is encountered
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if evaluating_parenthesis:
                output.append('*')
            if stack and stack[-1] == '(':
                stack.pop()
            i += 1
    # Pop any remaining operators from the stack and add them to the output queue
    while stack:
        print("final output: {}".format(output))
        print("final stack: {}".format(stack))
        output.append(stack.pop())
        i += 1
    return evaluate_rpn(output)