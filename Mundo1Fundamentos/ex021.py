# toque música com um programa python

import pygame

pygame.init()
pygame.mixer.music.load('nomeArquivoMusica')
pygame.mixer.music.play()
input()
pygame.event.wait()

