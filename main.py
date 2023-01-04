import cv2 as cv
import numpy as np

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from edges import bordas
from filters import filtros
from morf import morflogicas

# O sistema consiste em um conjunto de métodos que demonstram de forma simplicada a execução de métodos que a biblioteca OpenCV disponibiliza


def menu():
    print("Qual tipo de manipulação de imagens você deseja fazer?\n")
    print("1 - Aplicação de filtros em imagens")
    print("2 - Detecção de bordas")
    print("3 - Manipulação morfológicas")


menu()
opt = int(input("\nEscolha uma das opções: "))
print("\n---Escolha alguma imagem---\n")
janela_padrao = Tk().withdraw()
path = askopenfilename(filetypes=(
    ("Arquivos jpg", "*.jpg"), ("Arquivos png", "*.png")))
img = cv.imread(path)

if opt == 1:
    filtros.optionsFilter(img)
elif opt == 2:
    bordas.optionsBorder(img)
elif opt == 3:
    morflogicas.optionsMorf(img)
