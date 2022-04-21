import sys

class Queue:
    def __init__(self, path):
        self.values = []
        self.top = 0
        self.bottom = 0
        self.size = 0
        self.output = open(path, 'w')

    def set_size(self, cmd):
        if self.size != 0:
            self.error()
            return

        self.size = int(cmd.split(' ')[1]) + 1
        self.values = ['' for _ in range(self.size)]

    def pop(self):
        if self.size <= 0:
            self.error()
            return

        if self.top == self.bottom:
            self.underflow()
            return

        self.output.write(self.values[self.top] + '\n')
        self.top = (self.top + 1) % self.size

    def push(self, cmd):
        args = cmd.split(' ')

        if len(args) > 2 or self.size <= 0:
            self.error()
            return

        if (self.bottom + 1) % self.size == self.top:
            self.overflow()
            return

        self.values[self.bottom] = args[1]
        self.bottom = (self.bottom + 1) % self.size

    def print(self):
        if self.size == 0:
            self.error()
            return

        if self.top == self.bottom:
            self.empty()
            return

        if self.top < self.bottom:
            self.output.write(' '.join(self.values[self.top:self.bottom]) + '\n')
        elif self.bottom < self.top:
            self.output.write(' '.join(self.values[self.top:self.size] + self.values[:self.bottom]) + '\n')

    def overflow(self):
        self.output.write("overflow\n")

    def underflow(self):
        self.output.write("underflow\n")

    def empty(self):
        self.output.write("empty\n")

    def error(self):
        self.output.write("error\n")

    def finalize(self):
        self.output.close()

queue = Queue(sys.argv[2])

with open(sys.argv[1], 'r') as f:
    for cmd in f:
        cmd = cmd.strip('\n')

        if cmd == "":
            continue

        if len(cmd) >= 9 and cmd.startswith("set_size "):
            queue.set_size(cmd)
        elif cmd == "pop":
            queue.pop()
        elif cmd.startswith("push "):
            queue.push(cmd)
        elif cmd == "print":
            queue.print()
        else:
            queue.error()

queue.finalize()
