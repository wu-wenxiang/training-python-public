from stack_SStack import *
'''
后缀表达式的实现
'''

# 检查栈深
class ESStack(SStack):
    def depth(self):
        return len(self.elems)


# 括号配对问题
def check_pares(text):
    pares = "()[]{}"
    open_pares = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}  # 表示配对关系的字典

    def paretheses(text):   # 括号生成器，定义见后
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in pares:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in paretheses(text):  # 对 text 里各括号和位置迭代
        if pr in open_pares:  # 开括号，压进栈并继续
            st.push(pr)
        elif st.pop() != opposite[pr]:  # 不匹配就是失败，退出
            print("Unmatching is found at", i, "for", pr)
            return False
    # else 是一次括号配对成功，什么也不做，继续
    print("All paretheses are correctly matched.")
    return True


################################################
####### Suffix expression evaluator ############

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

# 后缀表达式的计算
def suf_exp_evaluator(exp):
    """exp is a list of items representing a suffix expression.
    This function evaluates it and return its value.
    """
    operators = "+-*/"
    st = ESStack()  # 扩充功能的栈，可用 depth() 检查栈内元素个数
    for x in exp:
        if not x in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError("Short of operand(s).")
        a = st.pop()  # second argument
        b = st.pop()  # first argument
        if x == "+":
            c = b + a
        elif x == "-":
            c = b - a
        elif x == "*":
            c = b * a
        elif x == "/":
            if a == 0: raise ZeroDivisionError
            c = b / a
        else:
            pass  # This branch is not possible
        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")


# end suf_exp_evaluator

def suffix_exp_calculator():
    """Repeatly ask for expression input until an 'end'."""
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end":
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)


def suffix_demo():
    print(suffix_exp_evaluator("1"))
    print(suffix_exp_evaluator("1 2 +"))
    print(suffix_exp_evaluator("1 3 + 2 *"))
#     print(suffix_exp_evaluator("1 3 + 2 5 - *"))


#####################################################
##### Transform infix expression to suffix expression

priority = {"(": 1, "+": 3, "-": 3, "*": 5, "/": 5}
infix_operators = "+-*/()"


def tokens(line):
    """ This function cannot deal with signed numbers,
    nor unary operators.
    """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:  # 运算符的情况
            yield line[i]
            i += 1
            continue
        j = i + 1
        while (j < llen and not line[j].isspace() and
               line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E') and  # 处理负指数
                    j + 1 < llen and line[j + 1] == '-'):
                j += 1
            j += 1
        yield line[i:j]  # 生成运算对象子串
        i = j


def trans_infix_suffix(line):
    st = SStack()
    llen = len(line)
    exp = []
    for x in tokens(line):  # tokens 是一个待定义的生成器
        if x not in infix_operators:  # 运算对象直接送出
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号的分支
            while not st.is_empty() and st.top() != "(":
                exp.append(st.pop())
            if st.is_empty():  # 没找到左括号，就是不配对
                raise SyntaxError("Missing \'(\'.")
            st.pop()  # 弹出左括号，右括号也不进栈
        else:  # 处理算术运算符，运算符都看作是左结合
            while (not st.is_empty() and
                   priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)  # 算术运算符进栈
    while not st.is_empty():  # 送出栈里剩下的运算符
        if st.top() == "(":  # 如果还有左括号，就是不配对
            raise SyntaxError("Extra \'(\' in expression.")
        exp.append(st.pop())
    return exp

def test_trans_infix_suffix(s):
    print(s)
    print(trans_infix_suffix(s))
    print("Value:", suf_exp_evaluator(trans_infix_suffix(s)))


def demo_trans():
    test_trans_infix_suffix("1.25")
    test_trans_infix_suffix("1 + 2")
    test_trans_infix_suffix("1 + 2 - 3")
    test_trans_infix_suffix("1 + 2 * 3")
    test_trans_infix_suffix("7. / 2 * 3")
    test_trans_infix_suffix("7.e-2/2*3")
    test_trans_infix_suffix("(1 + 2) * 3")
    test_trans_infix_suffix("1 + 2 * 3 - 5")
    test_trans_infix_suffix("13 + 2 * (3 - 5)")
    test_trans_infix_suffix("(1 + 2) * (3 - 5)")
    test_trans_infix_suffix("(1 + (2 * 3 - 5)) / .25")


if __name__ == "__main__":
#     check_pares("")
#     check_pares("()")
#     check_pares("([]{})")
#     check_pares("([]{}]")
#     check_pares("(abbvbb[hhh]jhg{lkii288}9000)000fhjsh")
#     check_pares("jkdsjckd(mfkk[fdjjfk],,,{kckjfc}jskdjkc]kkk")
 
    suffix_demo()
    # suffix_exp_calculator()