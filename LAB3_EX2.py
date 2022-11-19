list = []
list.append("A")
list.append("B")
list.append("C")
list.append("D")
list.append("E")
list.append("F")
len_list = len(list)

def showlist():
    print("Before Reverse")
    print("________________")
    print("Address | Array")
    for i in range(0,len_list):
        print(i,"      |  ",list[i])
    print("________________")

def showlistreverse():
    print("After Reverse")
    print("________________")
    print("Address | Array")
    for i in range(len_list-1, -1,-1):
        print(len_list-i-1, "      |  ", list[i])
    print("________________")

showlist()
print("\n\n")


class Stack:
    def __init__(self):
        self.items = list

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

showlistreverse()
s = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        s.push((do[1]))
        showlistreverse()
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
            len_list -= 1
            showlistreverse()
    elif operation == 'quit':
        break