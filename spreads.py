import gspread
import requests
import json
import time
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

#Se autentica
gc = gspread.authorize(credentials)

#abre a planilha através do id presente na url
wks = gc.open_by_key('1sk4CNJPf8Rt37QYJruexBSVtvObFtuM4a50scS2yh5c')

#abre primeira página da planilha
worksheet = wks.get_worksheet(0)

temperaturas = {'temperatura':[],'hora':[]}

for i in range(5):
    response = requests.get('http://127.0.0.1:8000/rooms/1')
    response = json.loads(response.text)
    temperatura = float(response['temperature'])
    temperaturas['temperatura'].append(temperatura)
    agora = str(response['time'])
    temperaturas['hora'].append(agora) 
    #construir arquivo csv caso esteja trabalhando com o pandas 
    #dataframe = pd.DataFrame(data = temperaturas)
    #dataframe.to_csv('temperaturas.csv', encoding='utf-8', index=False)
    print(temperaturas)
    time.sleep(4)

#Contador de colunas e celulas
colums = 1
cel = 1

for i in range(len(temperaturas['temperatura'])):
    #Atualiza a celula 2 da coluna 1 com a temperatura 
    worksheet.update_cell(cel, colums,temperaturas['temperatura'][i])
    #A coluna agora é a B
    colums = 2
    #Atualiza a celula 2 da coluna 2 com o valor da hora
    worksheet.update_cell(cel, colums,temperaturas['hora'][i])
    #A coluna agora é a A
    colums = 1 
    #Acrescenta mais um valor no numero da celula
    cel += 1

print('Tabela atualizada!')