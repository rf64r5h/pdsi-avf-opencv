import cv2 as cv
import numpy as np

# Exibir imagem original


def originImg(img):
    cv.imshow("Imagem Original", img)


# Filtro - imagem para cinza

# Podemos usar uma função cvtColor, onde passamos cv2.COLOR_BGR2GRAY como parâmetro.
def greyImg(img):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Imagem para cinza", imgGray)
    cv.waitKey(0)

# Filtro - img para HSV

# Podemos usar uma função cvtColor, onde passamos cv.COLOR_BGR2HSV como parâmetro.


def hsvImg(img):
    imgHsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("Imagem para HSV", imgHsv)
    cv.waitKey(0)

# Filtro - Desfocar imagem

# O desfoque é usado para remover o ruído extra da imagem, também chamado de suavização

# Vamos utilizar o método GaussianBlur


def imgBlur(img):
    imgBlur = cv.GaussianBlur(img, (3, 3), 0)
    cv.imshow("Imagem com Desfoque", imgBlur)
    cv.waitKey(0)


def optionsFilter(img):
    print("Qual Filtro você deseja aplicar na imagem?\n")
    print("1 - Filtro de imagem cinza")
    print("2 - Filtro para borrar a imagem (Gaussiano)")
    print("3 - Filtro para deixar a imagem em hsv")

    opt = int(input("\nEscolha uma das opções: "))
    if opt == 1:
        greyImg(img)
    elif opt == 2:
        imgBlur(img)
    elif opt == 3:
        hsvImg(img)
    else:
        print("Voce selecionou uma opção invalida")
