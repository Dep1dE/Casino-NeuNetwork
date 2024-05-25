import requests
import json
import time
import urllib.request

OddsHistory = [] #Список коэффициентов крашей
MainAnalisisList = []
number=0
MainRTP=0

def GetMainRTP():
    count=0;
    RTP=0
    global MainRTP
    for item in MainAnalisisList:
        try:
            RTP+=item[5]
            count+=1
        except:
            pass
    RTP=RTP/count
    MainRTP=RTP

#def GetRTPImpakt(games):

def WriteFile():
    file = open("history.txt", "w")
    for item in MainAnalisisList:
        file.write(str(item))
        file.write("\n")
    file.close()

def GetIntermediateRTP(count):
    RTP=0
    znam=count
    point=number
    while(count>0):
        try:
            RTP+=MainAnalisisList[point][5]
        except:
            pass
        point -= 1
        count -= 1
    RTP=RTP/znam
    return RTP

def GetIdInfo(id):
    list=[]
    url = "https://2cs.fail/api/crash/games/" + str(id)
    response = requests.get(url)
    data1 = json.loads(response.text)
    cashSum = 0
    vinSum = 0
    for item in data1['data']['bets']:
        if(item['winItemPrice'] is not None):
             vinSum += float(item['winItemPrice'])
        cashSum += float(item['itemsTotal'])
    rtp = 0
    rtp = vinSum/cashSum
    list.append(cashSum)
    list.append(vinSum)
    list.append(rtp)
    return list
    #print(list)

def GetFullHistoryInfo():
    URL_TEMPLATE = "https://2cs.fail/api/crash/games/current"
    r = requests.get(URL_TEMPLATE)
    data = json.loads(r.text) # получаем информацию от сайта(коэффициенты на которых произошел краш)

    global number

    for item in reversed(data['data']['history']):
        PersonalAnalisisList = []
        OddsHistory.append(item['crashedAt']) #добавляем коэффициенты в список
        PersonalAnalisisList.append(number) #добавляем номер в список
        PersonalAnalisisList.append(item['id']) #добавляем id в список
        PersonalAnalisisList.append(item['crashedAt'])  # добавляем коэффициент в список
        try:
            PersonalAnalisisList.extend(GetIdInfo(item['id']))
        except:
            pass
        number+=1
        print(PersonalAnalisisList)
        MainAnalisisList.append(PersonalAnalisisList)

def PrintStatistic(number):
    print(MainAnalisisList[number])
    GetMainRTP()
    print("MAIN RTP:", MainRTP)
    print("RTP-1:", GetIntermediateRTP(1))
    print("RTP-2:", GetIntermediateRTP(2))
    print("RTP-3:", GetIntermediateRTP(3))
    print("RTP-4:", GetIntermediateRTP(4))
    print("RTP-5:", GetIntermediateRTP(5))
    print("RTP-10:", GetIntermediateRTP(10))
    print("_________________________________________________________________________________")

#PreOnlaineAnalisis

GetFullHistoryInfo()

WriteFile()

#OnlaineAnalisis

idOneGame=0

while(True):
    URL_TEMPLATE = "https://2cs.fail/api/crash/games/current"
    r = requests.get(URL_TEMPLATE)
    data = json.loads(r.text)
    if(data['data']['game']['crashedAt'] is not None):        #data['data']['status'] == 3
        if(data['data']['game']['id'] != idOneGame):
            personalAnalisisList = []
            idOneGame = data['data']['game']['id']
            OddsHistory.append(data['data']['game']['crashedAt'])
            personalAnalisisList.append(number)
            personalAnalisisList.append(data['data']['game']['id'])
            personalAnalisisList.append(data['data']['game']['crashedAt'])
            cashSum = 0
            vinSum = 0

            time.sleep(1)
            r1 = requests.get(URL_TEMPLATE)
            data1 = json.loads(r1.text)
            for item in data1['data']['bets']:
                if (item['winItemPrice'] is not None):
                    vinSum += float(item['winItemPrice'])
                cashSum += float(item['itemsTotal'])
            rtp = 0
            rtp = vinSum / cashSum
            personalAnalisisList.append(cashSum)
            personalAnalisisList.append(vinSum)
            personalAnalisisList.append(rtp)
            MainAnalisisList.append(personalAnalisisList)
            PrintStatistic(number)
            number += 1
    else:
        idOneGame=0










#print("______________________________________________")
#for item in MainAnalisisList:
 #   print(item)
#sredRtp = 0
#for item in MainAnalisisList:
#    sredRtp += item[5]
#sredRtp = sredRtp/len(MainAnalisisList)
# print("++++++++++++++++++++++++++++++++++++++++++++++")
# GetMainRTP()
# print(MainRTP)
#print(sredRtp)
#GetIdInfo(4657367)





   #cofDataURL = "https://onemails.net/games/" + str(item['id']) #получаем ссылку на игру
   #g = requests.get(cofDataURL)
   #cofData = json.loads(g.text) #получаем информацию об игре





