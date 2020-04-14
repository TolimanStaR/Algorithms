import operator

polynom = str(input())
polynomial = str()

print('Expression:')
print(polynom)

operators = '^*/+-()'

for i in range(len(polynom)):
    if polynom[i] in operators:
        polynomial += ' ' + polynom[i] + ' '

    else:
        polynomial += polynom[i]

polynomial = polynomial.split()


class Stack(object):

    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def push(self, *args):
        for element in args:
            self.array.append(element)

    def pop(self):
        return self.array.pop(len(self.array) - 1)

    def last_element(self):
        return self.array[len(self.array) - 1]

    def __len__(self):
        return len(self.array)

    def show(self):
        print(*self.array)

    def is_empty(self):
        if len(self.array) < 1:
            return True
        return False


priority = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    ')': 0
}

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "^": pow
}

operator_sign = '^*/+-'

stack_for_polynomial = Stack()
stack_for_string = Stack()
string = str()


def get_string(polynomial):
    global string
    string = str()

    for sym in polynomial:

        if sym not in operators:
            string += sym + ' '

        if sym == '(':
            stack_for_polynomial.push(sym)

        if sym == ')':
            while stack_for_polynomial.last_element() != '(':
                string += stack_for_polynomial.pop() + ' '

            stack_for_polynomial.pop()

        if sym in operator_sign:
            while True:
                if not stack_for_polynomial.is_empty():
                    if priority[stack_for_polynomial.last_element()] >= priority[sym]:
                        string += stack_for_polynomial.pop() + ' '

                    else:
                        stack_for_polynomial.push(sym)
                        break
                else:
                    stack_for_polynomial.push(sym)
                    break

    while not stack_for_polynomial.is_empty():
        string += stack_for_polynomial.pop() + ' '

    print('Reverse Polish Notation:')
    print(string)
    return string


def calculate_value(string):
    string = string.split()

    for symbol in string:
        if symbol not in operator_sign:
            stack_for_string.push(int(symbol))

        elif symbol in operator_sign:
            second_number = stack_for_string.pop()
            first_number = stack_for_string.pop()
            result = action[symbol](first_number, second_number)

            stack_for_string.push(result)

    print('Result:')
    print(int(stack_for_string.pop()))


if __name__ == '__main__':
    calculate_value(get_string(polynomial))
