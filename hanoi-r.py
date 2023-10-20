def hanoi(n:int, a, buf, c):
    match n:
        case 1:
            print(a, "-->", c)
        case _:
            hanoi(n-1, a, c, buf) 
            hanoi(1, a, buf, c) 
            hanoi(n-1, buf, a, c) 

class Frame:
    def __init__(self, n, a, buf, c):
        self.pc = 0
        self.n = n
        self.a = a
        self.buf = buf
        self.c = c

    def step(self):
        self.pc += 1


def call(stack, n, a, buf, c):
    stack.append(Frame(n, a, buf, c))

def ret(stack):
    stack.pop()

def step(stack):
    stack[len(stack)-1].step()

def top(stack):
    return stack[len(stack)-1]

def hanoi_nr(n:int, a, buf, c):
    stack = []
    call(stack, n, a, buf, c)
    while stack != []:
        cur_frame = top(stack)
        match cur_frame.pc:
            case 0:
                if cur_frame.n == 1:
                    print(cur_frame.a, "->", cur_frame.c)
                    cur_frame.pc = 3
            case 1:
                call(stack, cur_frame.n - 1, cur_frame.a, cur_frame.c, cur_frame.buf)
            case 2:
                call(stack, 1, cur_frame.a, cur_frame.buf, cur_frame.c)
            case 3:
                call(stack, cur_frame.n - 1, cur_frame.buf, cur_frame.a, cur_frame.c)
            case 4:
                ret(stack)
        cur_frame.step()
                    
if __name__ == "__main__":
    hanoi_nr(4, "A", "B", "C")
