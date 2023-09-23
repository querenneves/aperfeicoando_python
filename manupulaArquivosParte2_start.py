import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\Pichau\\Documents\\Aperfeiçoando_python")

#CriaZipModo1()

def CriaZipModo2():
    with ZipFile("ArquicoZipModo2.zip", "w") as novoZip:
        novoZip.write("NovoArquivo.txt")
        novoZip.write("zipMode1.zip.zip")
        
#CriaZipModo2()

def DeletaArquivo():
    os.remove("ArquicoZipModo2.zip")

DeletaArquivo()
