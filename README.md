# Visão computacional - OpenCV

Repositorio que proproem apresentar 3 temas relacionado ao processamento de imagens com OpenCV para uma pessoa que está aprendendo processamento de imagens e videos.

## Breve resumo:

Primeiramente, vamos falar sobre sobre OpenCV que é a biblioteca mais popular em visão computacional. Ele originalmente foi escrito em `C` e `C++`. Mas também está disponível para o `Python` (no nosso caso iremos utilizar o Python) e outras linguagens. A biblioteca OpenCV é uma biblioteca altamente otimizada com foco principal em aplicativos em tempo real.

## Temas abordados:

- Detecção de bordas;
- Transformações morfológicas;
- Filtros básicos de imagem usando funções

## Explicação sobre as escolhas dos temas:

 A deteccção de bordas, transformações morfológicas e filtros para imagens são assuntos muitos famosos na área de visão computacional e também alguns desses assuntos estão alta de forma abrangente como a aplicação de filtros em imagens. Assim, pessoas que estão apredendo sobre visão computacional teram mais interesse no assunto.
 
 - <strong>Detecção de bordas</strong> é algo muito útil, porque nos ajuda e facilita na segmentação de objetos de uma forma muito direta em algumas situações (borda é um "lugar geométrico" que delimita um objeto qualquer).
 - <strong>Transformações morfológicas</strong> são uma classe de operações não lineares que nos permitem remover ruído de uma imagem e extrair a forma da mesma. Normalmente, essas transformações são aplicadas em imagens em escala de cinza ou binárizadas. 
 - <strong>Filtros</strong> são efeitos que podem altera as imagens em vários aspectos, alterando os controle de luz, cor, etc. Esse tema está bastente em alta com o avanço das redes sociais, principalmente o instagram que sempre teve o foco na postagens de fotos


## Instalação da biblioteca OpenCV no Python usando o pip:

`pip install opencv-python`


## Básico

### Importar a biblioteca OpenCV

`import cv2`

### Ler e mostrar uma imagem

Leitura (imread):

`
img = cv2.imread("Nome_da_imagem.jpg")
`

Exibição (imshow):

`
cv2.imshow("Nome_da_janela",img)
`




