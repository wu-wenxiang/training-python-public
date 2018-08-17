""" a stack class implemented using Python list 
"""

class StackUnderflow(ValueError):
    pass

# 用列表实现栈
class SStack(): 
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return self.elems == []
    def top(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems[len(self.elems)-1]
    def push(self, elem):
        self.elems.append(elem)
    def pop(self):
        if self.elems == []:
            raise StackUnderflow
        return self.elems.pop()

    
if __name__ == '__main__':
    st = SStack()
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.pop())
    print(st.is_empty())
    st.top()

