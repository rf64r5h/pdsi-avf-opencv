import cv2 as cv
import numpy as np

# Vamos utilizar o método Canny para a detecção de bordas(edges)
#
# Método Canny: cv.Canny(img,threshold1,threshold2)
#
# threshold1,threshold2: São Diferentes valores de limiares diferentes para cada imagem
# O menor valor entre threshold1 e threshold2 é usado para ligação de borda. O maior valor é usado para encontrar segmentos iniciais de arestas fortes


def canny(img):
    imgCanny = cv.Canny(img, 100, 100)
    cv.imshow("Deteccaoo de bordas", imgCanny)
    cv.waitKey(0)


def laplacian(img):
    ddepth = cv.CV_16S
    kernel_size = 3

    blur = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

    dst = cv.Laplacian(gray, ddepth=ddepth, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)

    cv.imshow("Laplacian", abs_dst)
    cv.waitKey(0)


def optionsBorder(img):
    print("Qual tipo de manipulação de borda voce deseja aplicar na imagem?\n")
    print("1 - Detecção de borda na imagem com Canny")
    print("2 - Detecção de borda na imagem com Laplacian")

    opt = int(input("\nEscolha uma das opções: "))
    if opt == 1:
        canny(img)
    elif opt == 2:
        laplacian(img)
    else:
        print("Voce selecionou uma opção invalida")
