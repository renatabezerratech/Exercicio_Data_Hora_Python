# Para trabalhar com data é preciso importar o módulo datetime;
import datetime

# Para trabalhar a variável, precisa declarar o valor e em seguida dizer o que quer:
x = datetime.datetime.now()   
print(x)   # Para exibir a data e a hora atual

x = datetime.datetime.now()   
print(x.strftime("%A"))   # Para exibir dia da semana 
                          # O método strftime() formata a data em string

#depois

from datetime import date  #Aqui importo o módulo datetime e defino o nome da classe -> date
from datetime import time  #Aqui importo o módulo datetime e defino o nome da classe -> time
from datetime import datetime  # Aqui importo o módulo datetime e defino o nome da classe ->datetime

def trabalhaData():   # Crio a função trabalhaData sem parâmetros
    hoje = date.today()   # Crio a variável hoje e atribuo o valor date.today() que é a data de hoje
    print("Hoje: ",hoje)  # Imprime normal
    print("Data dividida: ",hoje.day, hoje.month, hoje.year) # Imprime a data organizada e dividida
    diaSemana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    print("Hoje é ",diaSemana[hoje.weekday()]) # Se eu quiser localizar o dia da semana por array;
    data = datetime.now()      # Chama a data e a hora
    print("Data e hora atual: ",data)
    hora = datetime.time(data) # Usa o valor da variável data para chamar só a hora
    print("Hora atual: ",hora)
  
trabalhaData()   # Chama a função
