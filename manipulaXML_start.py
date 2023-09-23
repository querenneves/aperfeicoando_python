import xml.dom.minidom

def manipulaXML():
    try:
        doc = xml.dom.minidom.parse("C:\\Users\\Pichau\\Documents\\Aperfeiçoando python\\exemplo.html")

        print("Nome da primeira tag: ", doc.firstChild.tagName)
        primeiroNome = doc.getElementsByTagName("firstname")
        if primeiroNome:
            print("O primeiro nome é: ", primeiroNome[0].firstChild.nodeValue)

        for skill in doc.getElementsByTagName("skill"):
            name = skill.getAttribute("name")
            if name:
                print("Skill encontrado: ", name)
    # tratamento de exceção para capturar erros
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao manipular o XML:", str(e))

manipulaXML()
