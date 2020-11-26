#Stack operations - Save this as 'stack.py
class Stack:
    def __init__(self):
        self.st = [ ]
    def isempty(self):
        return self.st
    def push(self, element):
        self.st.append(element)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
    def peep(self):
        n = len(self.st)
        return self.st[n-1]
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.st.index(element)
            except ValueError:
                return -2
    def display(self):
        return self.st
    
s = Stack()
print(s.display())