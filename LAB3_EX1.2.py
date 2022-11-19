list = []
list.append("A")
list.append("B")
list.append("C")
list.append("D")
list.append("E")
list.append("F")
len_list = len(list)
print("### FIFO  FIFO  FIFO  FIFO  FIFO ###")
def showlist():
    print("________________")
    print("Address | Array")
    for i in range(0,len_list):
        print(i,"      |  ",list[i])
    print("________________")

while True:
    showlist()
    pop = input("Do you want to pop ? (Y/N) : ")
    if pop == "Y":
        list.reverse()
        list.pop()
        len_list -= 1
        list.reverse()
        if len_list == 0:
            exit()
    elif pop == "N":
        exit()
    else:
        print("Wrong input!!")