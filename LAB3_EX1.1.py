list = []
list.append("A")
list.append("B")
list.append("C")
list.append("D")
list.append("E")
list.append("F")
len_list = len(list)
print("### FILO  FILO  FILO  FILO  FILO ###")
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
        list.pop()
        len_list -= 1
        if len_list == 0:
            break
    elif pop == "N":
        break
    else:
        print("Wrong input!!")
