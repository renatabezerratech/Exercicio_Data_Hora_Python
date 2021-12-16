# Esse é um exercício feito no LinkedIn Learning;
# Mostra um exemplo de como podemos manipular os dados de data e hora;

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta # Classe que permite operações matemáticas com datas;

def faltamDias(ano,mes,dia):
    hoje = date.today()
    dataProcurada = date(ano,mes,dia)
    quantosDias = dataProcurada - hoje  # Operação;
    mensagemRetorno = "Faltam " + str(quantosDias).replace("days, 0:00:00","")+"dias para a data."
    print(mensagemRetorno)

# str transforma o dado em uma string, pois não pode somar dados com tipos diferentes;
# replace serve para mudar o retorno no terminal, nesse caso, tirar o primeiro e colocar o segundo;

faltamDias(2021,12,20)
