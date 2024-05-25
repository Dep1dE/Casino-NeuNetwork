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
    url = "https://onemails.net/games/" + str(id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://csgoad.run',
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzA3OTIwLCJpYXQiOjE3MDg2NjM4NTIsImV4cCI6MTcwOTUyNzg1Mn0.kwrEdTcr0d6HjQO4lqkdZKkXsMosl8rzQ0A9-ZrsoJc'
    }
    response = requests.get(url, headers=headers)
    data1 = json.loads(response.text)
    cashSum = 0
    vinSum = 0
    for item in data1['data']['bets']:
        #print(item['deposit']['amount'])
        #print(item['withdraw']['amount'])
        #print("_________________________________")
        if(item['withdraw']['amount'] is not None):
            vinSum += item['withdraw']['amount']
        cashSum += item['deposit']['amount']
    #rtp = vinSum/cashSum
    rtp = 0
    rtp = vinSum/cashSum
    list.append(cashSum)
    list.append(vinSum)
    list.append(rtp)
    return list
    #print(list)

def GetFullHistoryInfo():
    URL_TEMPLATE = "https://onemails.net/crash/state"
    r = requests.get(URL_TEMPLATE)
    data = json.loads(r.text) # получаем информацию от сайта(коэффициенты на которых произошел краш)
    global number

    for item in reversed(data['data']['history']):
        PersonalAnalisisList = []
        OddsHistory.append(item['crash']) #добавляем коэффициенты в список
        PersonalAnalisisList.append(number) #добавляем номер в список
        PersonalAnalisisList.append(item['id']) #добавляем id в список
        PersonalAnalisisList.append(item['crash'])  # добавляем коэффициент в список
        if(number>20):
            try:
                PersonalAnalisisList.extend(GetIdInfo(item['id']))
            except:
                pass
        number+=1
        print(PersonalAnalisisList)
        MainAnalisisList.append(PersonalAnalisisList)

GetFullHistoryInfo()

idOneGame=0

while(True):
    URL_TEMPLATE = "https://onemails.net/crash/state"
    r = requests.get(URL_TEMPLATE)
    data = json.loads(r.text)
    if(data['data']['crash'] is not None):        #data['data']['status'] == 3
        if(data['data']['delta'] != idOneGame):
            personalAnalisisList = []
            idOneGame = data['data']['delta']
            OddsHistory.append(data['data']['crash'])
            personalAnalisisList.append(number)
            personalAnalisisList.append(data['data']['bets'][0]['id'])
            personalAnalisisList.append(data['data']['crash'])
            cashSum = 0
            vinSum = 0
            r1 = requests.get(URL_TEMPLATE)
            data1 = json.loads(r1.text)
            for item in data1['data']['bets']:

                if (item['withdraw']['amount'] is not None):
                    vinSum += item['withdraw']['amount']
                #cashSum += item['deposit']['amount']
            rtp = 0
            cashSum=data1['data']['statistic']['totalDeposit']
            rtp = vinSum / cashSum
            personalAnalisisList.append(cashSum)
            personalAnalisisList.append(vinSum)
            personalAnalisisList.append(rtp)
            MainAnalisisList.append(personalAnalisisList)
            print(MainAnalisisList[number])
            GetMainRTP()
            print("MAIN RTP:", MainRTP)
            print("RTP-3:", GetIntermediateRTP(3))
            print("RTP-5:", GetIntermediateRTP(5))
            print("______________________________________________")
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
print("++++++++++++++++++++++++++++++++++++++++++++++")
#print(sredRtp)
#GetIdInfo(4657367)





   #cofDataURL = "https://onemails.net/games/" + str(item['id']) #получаем ссылку на игру
   #g = requests.get(cofDataURL)
   #cofData = json.loads(g.text) #получаем информацию об игре
print(OddsHistory)




