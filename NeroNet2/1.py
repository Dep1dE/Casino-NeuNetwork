import math
data_list = [] # Список со всей изначальной инфой из файла
link = "D:\WorkTable\information\Projects\Python_Parser2\history.txt" # Ссылка на файл с инфой
SampleSize=20 # Размер выборки которую будем анализировать
FirstLevel=[] # Первый уровень
SecondLevel=[] # Второй уровень

def PrintList(list): # Вывод списка
    for item in list:
        print(item)

def GetInformationFromFile():
    with open(link, 'r') as file:
        for line in file:
            line = line.strip() # Удаляем символы переноса строки и пробелы в начале и конце строки
            line = line[1:-1] # Удаляем квадратные скобки в начале и конце строки
            elements = line.split(', ') # Разбиваем строку по запятым и пробелам
            elements = [eval(elem) for elem in elements] # Преобразуем строки в числа, где это возможно
            data_list.append(elements)

def MakeFirstLevel():
    for item in data_list[10:20]:
        FirstLevel.append(item)


GetInformationFromFile() # Заполняем список информацией
MakeFirstLevel()

PrintList(data_list)
print("__________________________________________________________")
PrintList(FirstLevel)


# Сapture=SampleSize
# while Сapture<data_list.__len__():
#     print(data_list[Сapture])
#     Сapture+=1
