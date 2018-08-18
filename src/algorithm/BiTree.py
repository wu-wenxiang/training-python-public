""" Implementing binary trees as embedded list
"""

def BiTree(data, left, right):
    return [data, left, right]

def is_empty_BiTree(bitree):
    return bitree == []

def root(bitree):
    return bitree[0]

def leftch(bitree):
    return bitree[1]

def rightch(bitree):
    return bitree[2]

def set_root(bitree, data):
    bitree[0] = data

def set_leftch(bitree, left):
    bitree[1] = left

def set_rightch(bitree, right):
    bitree[2] = right

###############################################
#### Functions for ############################
#### building and manipulating ################
#### mathematical expressions  ################
from numbers import Number

def make_sum(a, b):
    return ['+', a, b]

def make_prod(a, b):
    return ['*', a, b]

def make_diff(a, b):
    return ['-', a, b]

def make_div(a, b):
    return ['/', a, b]

def is_basic_exp(a):
    return not isinstance(a, list)

def is_compose_exp(a):
    return isinstance(a, list)

def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)
        
def eval_sum(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a + b
    if isinstance(a, Number) and a == 0:
        return b
    if isinstance(b, Number) and b == 0:
        return a
    return make_sum(a, b)

def eval_diff(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a - b
    if isinstance(a, Number) and a == 0:
        return -b
    if isinstance(b, Number) and b == 0:
        return a
    return make_diff(a, b)

def eval_prod(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a * b
    if (isinstance(a, Number) and a == 0 or
        isinstance(b, Number) and b == 0):
        return 0
    if isinstance(a, Number) and a == 1:
        return b
    if isinstance(b, Number) and b == 1:
        return a
    return make_prod(a, b)

def eval_div(a, b):
    if isinstance(a, Number) and isinstance(b, Number):
        return a / b
    if isinstance(a, Number) and a == 0:
        return 0
    if isinstance(b, Number) and b == 0:
        raise ZeroDivisionError
    if isinstance(b, Number) and b == 1:
        return a
    return make_div(a, b)
    
   
if __name__ == '__main__':
    t1 = BiTree(2, BiTree(4, [], []), BiTree(8, [], []))
    print(t1)
#     set_leftch(leftch(t1), BiTree(5, [], []))
#     print(t1)
# 
#     e1 = make_prod(make_sum(2, 3), make_diff(4, 5))
#     e2 = make_prod(make_diff(make_prod(2, 'a'), 3), make_diff(4, 5))
#     e3 = make_div(make_sum(make_prod(2, 7), make_div(0, 'b')), make_div('a', 1))
# 
#     ret = eval_exp(['+', 2, 3])
#     print(ret)
#     eval_exp(['$', 2, 3]) # This will cause an exception because $ is not a valid operator
#     

