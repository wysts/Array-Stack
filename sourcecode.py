def Pop(stackPop):
    del stackPop[-1]


def Push(stackPush, innit):
    stackPush.append(innit)


def Top(stackTop):
    return stackTop[-1:]

stack = []
Push(stack, 10)
Push(stack, 9)
Push(stack, 8)
Push(stack, 7)

print("first stack" ,stack)
print("Top stack :"  ,Top(stack))

Pop(stack)
Pop(stack)
Pop(stack)

print("")
print("second stack" ,stack)
print("Top stack :"  ,Top(stack))

Pop(stack)
print("")
print("empty stack" ,stack)
