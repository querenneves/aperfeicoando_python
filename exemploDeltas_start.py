from datetime import date, time, datetime, timedelta

def QuantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)

    qtosDias = dataProcurada - hoje

    mensagemRetorno = "Faltam " + str(qtosDias.days).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")

    print(mensagemRetorno)

QuantosDiasFaltam(2030, 10, 29)
