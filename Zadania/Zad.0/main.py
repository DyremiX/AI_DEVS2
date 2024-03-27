import requests


url = 'https://tasks.aidevs.pl'
data = "{\"apikey\": \"TOKEN\"}"

#Najpierw pobieramy token autoryzacyjny 
response = requests.post(url + '/token/helloapi',data)
token_auth = response.json()['token']

print(response.text)

#Potem pobieramy zadanie
quest = requests.get(url + '/task/' + token_auth)

print(quest.text)

#szykujemy odpowiedź
data = "{\"answer\": \"" + quest.json()["cookie"] +"\"}"

#Odpowiadamy
answer = requests.post(url + '/answer/' + token_auth, data)

print(answer.text)
