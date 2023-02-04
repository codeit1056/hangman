import pygame
import sys
import hangman_pygame_words as words
pygame.init()

WIDTH,HEIGHT = 800,600
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()

font = pygame.font.Font('hangman_assets/hangman_font.ttf',15)

button_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
button_radius = 20
buttons = []

def draw_buttons():
    for button in range(10):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,350),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,350),button_radius,4))
    for button in range(10):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,400),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,400),button_radius,4))
    for button in range(6):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,450),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,450),button_radius,4))

    for letter in button_letters:
        letter_ = font.render(letter,True,BLACK)
        for button in buttons:
            letter_rect = letter_.get_rect(center = (button.centerx,button.centery))
            window.blit(letter_,letter_rect)



def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        window.fill(WHITE)
        draw_buttons()
        pygame.display.update()
        clock.tick(FPS)

run()