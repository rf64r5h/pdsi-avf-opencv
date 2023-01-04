import cv2 as cv
import numpy as np


def dilate(img, k, i):
    # Montar uma matriz de tamanho k por k chamada kernel
    kernel = np.ones((k, k), np.uint8)
    # Implementar o método do opencv para dilatar a imagem
    img_dilation = cv.dilate(img, kernel, iterations=i)
    cv.imshow("Imagem dilatada", img_dilation)
    cv.waitKey(0)


def erosin(img, k, i):
    # Montar uma matriz de tamanho k por k chamada kernel
    kernel = np.ones((k, k), np.uint8)
    # Implementar o método do opencv para aplicar erosão na imagem
    img_erosion = cv.erode(img, kernel, iterations=i)
    cv.imshow("Imagem com erosao", img_erosion)
    cv.waitKey(0)


def optionsMorf(img):
    print("Qual tipo de transformação morfológicas você deseja aplicar na imagem?\n")
    print("1 - Dilatação da imagem")
    print("2 - Erosão da imagem")
    opt = int(input("\nEscolha uma das opções: "))
    k = int(input("Escolha o tipo de matriz (ex.: 3, 5, 7): "))
    i = int(input("Escolha a quantidade de interações(ex.: 1): "))

    if opt == 1:
        dilate(img, k, i)
    elif opt == 2:
        erosin(img, k, i)
    else:
        print("Voce selecionou uma opção invalida")
