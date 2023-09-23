from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs:
            for a in attrs:
                print("Valores encontrados: ", a[0], " = ", a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada!")

    def handle_comment(self, data):
        print("Comentário encontrado.")

    def handle_data(self, data):
        print("Valores encontrados.")
        if data.isspace():
            print("O valor encontrado é um espaço.")
        else:
            print("O valor encontrado é: ", data)

def meuObjeto():
    meuparser1 = meuParser()
    with open("C:\\Users\\Pichau\\Documents\\Aperfeiçoando python\\exemplo.html", "r") as arquivo:
        dados = arquivo.read()
        meuparser1.feed(dados)

meuObjeto()
