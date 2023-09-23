def EscreveArquivo():
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.write("Linha gerada com a função 'EscrevaArquivo' \r\n")

    arquivo.close()

def AlteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.write("Linha gerada com a função 'AlteraArquivo' \r\n")

    arquivo.close()

AlteraArquivo()