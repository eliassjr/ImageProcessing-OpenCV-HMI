import pygame
import cv2
from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
from PIL import Image


pygame.init()

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (176, 196, 222)
azul2 = (100,149,237)



def texto(msg, cor, tam, x, y):
    fonte = pygame.font.Font(None, tam)
    texto1 = fonte.render(msg, True, cor)
    janela.blit(texto1, [x, y])

def selecao_arquivo():
## Comando Para Selecionar o Arquivo

    arquivo = filedialog.askopenfilename()
    img = cv2.imread(arquivo)
    redimensionar = cv2.resize(img, (500, 500))
    cv2.imwrite("b.png", redimensionar)

## Comando para Plotar a Imagem Selecionada
    image = pygame.image.load(r'b.png')
    janela.blit(image, (25, 200))

## Comando Para Criar o Histograma
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
         histr = cv2.calcHist([img], [i], None, [256], [0, 256])
         plt.plot(histr, color=col)
         plt.xlim([0, 256])
    figure = plt.figure(1)
    figure.set_size_inches(5, 3)
    plt.savefig('Histograma.png', format='png')
    plt.clf()

    img = cv2.imread('Histograma.png')
    redimensionar = cv2.resize(img, (300, 200))
    cv2.imwrite("Histograma.png", redimensionar)

    image = pygame.image.load(r'histograma.png')
    janela.blit(image, (550, 200))

def selecao_mouse(x,y):

    ## Pegas as coornedas x,y
    selecao = True
    while selecao:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())
                if (x > 25 and x < 525 and y > 200 and y < 700):
                    selecao = False
    xpos = x-25
    ypos = y-250

    ## Realiza o Recorte da Imagem
    image1 = Image.open('b.png')
    croppedIm = image1.crop((xpos - 70, ypos - 70, xpos + 70, ypos + 70))
    croppedIm.save('Recorte.png')

    ## Realiza a ampliação da imagem
    img = cv2.imread("Recorte.png")
    zoom = cv2.resize(img, (500, 500), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("b.png", zoom)

    ## Plota a imagem
    image = pygame.image.load(r'b.png')
    janela.blit(image, (25, 200))

    ## Comando Para Criar o Histograma
    img = cv2.imread("b.png")
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    figure = plt.figure(1)
    figure.set_size_inches(5, 3)
    plt.savefig('Histograma1.png', format='png')
    plt.clf()

    img = cv2.imread('Histograma1.png')
    redimensionar = cv2.resize(img, (300, 200))
    cv2.imwrite("Histograma1.png", redimensionar)

    image = pygame.image.load(r'histograma1.png')
    janela.blit(image, (550, 200))

def adicao():
    ##Comando para abrir a imagem
    img = cv2.imread("b.png")
    ##Somar a imagem
    img2b = cv2.add(img, img)
    ##Salvar a imagem
    cv2.imwrite("c.png", img2b)
    ##Plotar a imagem
    image = pygame.image.load(r'c.png')
    janela.blit(image, (900, 200))


    img = cv2.imread("c.png")
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    figure = plt.figure(1)
    figure.set_size_inches(5, 3)
    plt.savefig('Histograma2.png', format='png')
    plt.clf()

    img = cv2.imread('Histograma2.png')
    redimensionar = cv2.resize(img, (300, 200))
    cv2.imwrite("Histograma2.png", redimensionar)

    image = pygame.image.load(r'histograma2.png')
    janela.blit(image, (550, 500))

def equalizacao():
    ## Abre a imagem
    img = cv2.imread("b.png")

    ## Realiza a equalização
    imgy = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)  # para equalização de 1 canal
    imgy2 = imgy[:, :, 1]  # somente com a luminância, não com o H ou S
    imgy1 = imgy.copy()

    equ = cv2.equalizeHist(imgy2)
    imgy1[:, :, 1] = equ
    imgy3 = cv2.cvtColor(imgy1, cv2.COLOR_HLS2RGB)  # converte P&B



    ##Calcula o Histograma
    h2 = cv2.calcHist([equ], [0], None, [256], [0, 256])
    plt.plot(h2)
    figure = plt.figure(1)
    figure.set_size_inches(5, 3)
    plt.savefig('Histograma3.png', format='png')
    plt.clf()

    ##Salva o Histograma
    img = cv2.imread('Histograma3.png')
    redimensionar = cv2.resize(img, (300, 200))
    cv2.imwrite("Histograma3.png", redimensionar)

    ##Plota o histograma
    image = pygame.image.load(r'histograma3.png')
    janela.blit(image, (550, 500))

    ##Salva a imagem
    plt.imshow(imgy3)
    plt.axis('off')
    figure.set_size_inches(6.5, 6.5)
    plt.savefig('Equalizacao.png', format='png')
    plt.clf()

    ## Realiza o Recorte da Imagem
    image1 = Image.open('Equalizacao.png')
    croppedIm = image1.crop((83,78,583,578))
    croppedIm.save('Equalizacao.png')


    ## Realiza a ampliação da imagem
    img = cv2.imread("Equalizacao.png")
    zoom = cv2.resize(img, (500, 500), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("Equalizacao.png", zoom)

    ## Plota a Imagem
    image = pygame.image.load(r'Equalizacao.png')
    janela.blit(image, (900, 200))


janela = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Tela IHM")
janela.fill(azul)

codigo = True
while codigo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            codigo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            print(pygame.mouse.get_pos())
            if x > 25 and y > 50 and x < 245  and y < 90:
                selecao_arquivo()
            if x > 280 and y > 50 and x < 500  and y < 90:
                selecao_mouse(x,y)
            if x > 900 and y > 50 and x < 1150  and y < 90:
                adicao()
            if x > 1090 and y > 50 and x < 1350  and y < 90:
                equalizacao()

    pygame.draw.rect(janela, azul2, [25,50,220,40]) ## (posx, posy, tamx, tamy)
    texto("Seleção de Imagem", branco, 30, 40, 60)

    pygame.draw.rect(janela, azul2, [25, 120, 110, 40])  ## (posx, posy, tamx, tamy)
    texto("Figura 1", branco, 30, 40, 130)

    pygame.draw.rect(janela, azul2, [280, 50, 220, 40])  ## (posx, posy, tamx, tamy)
    texto("Seleção Mouse", branco, 30, 310, 60)

    pygame.draw.rect(janela, azul2, [900, 50, 150, 40])  ## (posx, posy, tamx, tamy)
    texto("Adição", branco, 30, 940, 60)

    pygame.draw.rect(janela, azul2, [1090, 50, 260, 40])  ## (posx, posy, tamx, tamy)
    texto("Equalização Histograma", branco, 30, 1100, 60)

    pygame.draw.rect(janela, azul2, [550, 120, 150, 40])  ## (posx, posy, tamx, tamy)
    texto("Histograma 1", branco, 30, 560, 130)

    pygame.draw.rect(janela, azul2, [550, 430, 150, 40])  ## (posx, posy, tamx, tamy)
    texto("Histograma 2", branco, 30, 560, 440)

    pygame.draw.rect(janela, azul2, [900, 120, 110, 40])  ## (posx, posy, tamx, tamy)
    texto("Figura 2", branco, 30, 918, 130)




    pygame.display.update()

pygame.quit()