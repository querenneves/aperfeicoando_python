from os import path
import time

def DadosArquivo():
    ArquivoExiste = path.exists("NovoArquivo.txt")
    Diretorio = path.isdir("NovoArquivo.txt")
    pathArquivo = path.realpath("NovoArquivo.txt")
    pathRelativo = path.realpath("NovoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(ArquivoExiste)
    print(Diretorio)
    print(pathArquivo)
    print(pathRelativo) 
    print(dataCriacao)
    print(dataModificacao)

DadosArquivo()
