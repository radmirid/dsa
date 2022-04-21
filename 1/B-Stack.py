import sys

class Stack:
    def __init__(self):
        self.values = []
        self.top = 0
        self.size = 0

    def set_size(self, cmd):
        if self.size != 0:
            self.error()
            return

        self.size = int(cmd.split(' ')[1])
        self.values = ['' for _ in range(self.size)]

    def pop(self):
        if self.size <= 0:
            self.error()
            return

        if self.top == 0:
            self.underflow()
            return
        
        self.top -= 1
        print(self.values[self.top]);

    def push(self, cmd):
        args = cmd.split(' ')

        if len(args) > 2 or self.size <= 0:
            self.error()
            return
        
        if self.top >= self.size:
            self.overflow()
            return

        self.values[self.top] = args[1]
        self.top += 1

    def print(self):
        if self.size == 0:
            self.error()
            return

        if self.top == 0:
            self.empty()
            return

        if self.top > self.size:
            self.overflow()
            return

        print(' '.join(self.values[:self.top]))

    def overflow(self):
        print("overflow")

    def underflow(self):
        print("underflow")

    def empty(self):
        print("empty")

    def error(self):
        print("error")

stack = Stack()

for cmd in sys.stdin:
    cmd = cmd.strip('\n')

    if cmd == "":
        continue

    if len(cmd) >= 9 and cmd.startswith("set_size "):
        stack.set_size(cmd)
    elif cmd == "pop":
        stack.pop()
    elif cmd.startswith("push "):
        stack.push(cmd)
    elif cmd == "print":
        stack.print()
    else:
        stack.error()
