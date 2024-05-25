import math
data_list = []
d=0


with open('D:\WorkTable\information\Projects\Python_Parser2\history.txt', 'r') as file:
    for line in file:
        line = line.strip()  # Удаляем символы переноса строки и пробелы в начале и конце строки
        line = line[1:-1]  # Удаляем квадратные скобки в начале и конце строки
        elements = line.split(', ')  # Разбиваем строку по запятым и пробелам
        elements = [eval(elem) for elem in elements]  # Преобразуем строки в числа, где это возможно
        data_list.append(elements)


def GetIntermediateRTP(count, position):
    RTP=0
    znam=count
    point=position
    while(count>0):
        try:
            RTP+=data_list[point][5]
        except:
            pass
        point -= 1
        count -= 1
    RTP=RTP/znam
    return RTP

def MakeW1(u):
    w1 = []
    i = 20+u
    while i < 40+u:
        personal = []
        j=1
        while j < 21:
            personal.append(GetIntermediateRTP(j, i))
            j += 1
        w1.append(personal)
        i += 1
    return w1

def PrintAll():
    print("Print main list")
    for item in data_list:
        print(item)
    print("__________________________________________________________")
    print("Print first level")
    for item in first:
        print(item)
    print("__________________________________________________________")
    print("Print first weight")
    for item in w1:
        print(item)
    print("__________________________________________________________")
    print("Main RTP")
    print(GetMainRTP(11))
    print("__________________________________________________________")
    print("Print second level")
    for item in second:
        print(item)
    print("__________________________________________________________")
    print("Result")
    print(GetResult())

def TransformationFirstLevel(first):
    for item in first:
        if float(item[1]) >= 2:
            item[1] = 1
        else:
            item[1] = float(item[1])-1
    return first

def TransformationW(w1):
    i = 0
    s=11
    while i < 10:
        RTP=GetMainRTP(s+i)
        personal = []
        j = 0
        while j < 10:
            if(w1[j][i] >= RTP):
                personal.append(-(w1[i][j]-RTP))
            else:
                personal.append(abs(w1[i][j]-RTP))
            j += 1
        w1[i]=personal
        i += 1
    return w1

def GetMainRTP(count):
    RTP=0
    znam=count
    count=count-1
    point=count
    while(count>=0):
        try:
            RTP+=data_list[count][5]
        except:
            pass
        point -= 1
        count -= 1
    RTP=RTP/znam
    return RTP

def MakeSecondLevel(first, w1):
    i = 0
    second=[]
    while i < 10:
        personal = []
        A=first[i][1]
        X=0
        j=0
        while j < 10:
            X+=w1[i][j]
            j += 1
        sigmoid=1 / (1 + math.exp(A*X+d))
        second.append(sigmoid)
        i += 1
    return second

def GetResult(second):
    index=1
    i=0
    max=-1
    while i < 10:
        if second[i]>max:
            max=second[i]
            index=i
        i += 1
    index=1+index/10
    return index


print("Print main list")
for item in data_list:
    print(item)
print("__________________________________________________________")


u=0
while u<40:
    w1 = []
    first = []
    second = []
    n=20+u
    for item in data_list[n:41+u]:
        personfirst = []
        personfirst.append(item[0])
        personfirst.append(item[2])
        first.append(personfirst)
    w1=MakeW1(u)
    y=[]
    y.extend(TransformationFirstLevel(first))
    first.clear()
    first=y
    h=[]
    h.extend(TransformationW(w1))
    w1.clear()
    w1=h
    sec=[]
    sec.extend(MakeSecondLevel(first, w1))
    second.clear()
    second=sec
    result=GetResult(second)
    d=d+float(data_list[n][2])-result
    u += 1
    print("Print first level:")
    for item in first:
        print(item)
    print("__________________________________________________________")
    print("Print first weight:")
    for item in w1:
        print(item)
    print("__________________________________________________________")
    print("Print second level:")
    for item in second:
        print(item)
    print("__________________________________________________________")
    print("My result:")
    print(result)
    print("Real result:")
    print(data_list[n][2])
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

