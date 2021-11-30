import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt

scope = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Teste Python").sheet1


temp = sheet.col_values(1)
time = sheet.col_values(2)

t = []

for i in temp:
    t.append(float(i))

plt.title("Monitoramento de temperatura")
plt.ylabel("Temperatura / °C")
plt.xlabel("Hora")
plt.axis(ymin=0.0, ymax=40.0)
plt.plot(time, t, label="Temperaturas", marker="o")
plt.legend()
plt.grid(True)

plt.show()

'''
scopes = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
json_file = "credentials.json"
'''


"""
def login():
    credentials = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    return gc

def leitor(aba):
    gc = login()
    planilha = gc.open("data")
    aba = planilha.worksheet("Página1")
    dados = aba.get_all_records()
    df = pd.DataFrame(dados)
    return df

def escritor(lista):
    gc = login()
    planilha = gc.open('Nome da Planilha')
    planilha = planilha.worksheet('Nome da Aba')
    planilha.append_row(lista, value_input_option='USER_ENTERED')
"""