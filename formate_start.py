from datetime import datetime

def FormataDataHora():


    hoje = datetime.now()

    print(hoje.strftime("O ano é: %y"))

    print(hoje.strftime("Data e hora local: %c"))

    print(hoje.strftime("A hora atual é:  %I: %M: %S: %p"))

FormataDataHora()