import pygame
import sys
import hangman_pygame_words as words
import random
pygame.init()

WIDTH,HEIGHT = 800,600
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()

font = pygame.font.Font('hangman_assets/hangman_font.ttf',15)
gap_font = pygame.font.Font('hangman_assets/hangman_font.ttf',100)

button_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
button_radius = 20
buttons = []
buttons_and_letters = []

random_word = random.choice(words.words_list)
random_word_lst = list(random_word)

def draw_buttons(button_letters):
    for button in range(10):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,350),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,350),button_radius,4))
    for button in range(10):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,400),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,400),button_radius,4))
    for button in range(6):
        pygame.draw.circle(window,BLACK,((button * 65) + 110,450),button_radius,4)
        buttons.append(pygame.draw.circle(window,BLACK,((button * 65) + 110,450),button_radius,4))


    for letter, button in zip(button_letters, buttons):
        buttons_and_letters.append([button,letter])
        letter_ = font.render(letter,True,BLACK)
        letter_rect = letter_.get_rect(center = (button.centerx,button.centery))
        window.blit(letter_,letter_rect)

def make_gaps():
    gaps = []
    for letter in random_word_lst:
        gaps.append('_')
    for gap in gaps:
        for i in range(len(random_word_lst)):
            gap_place = pygame.image.load('hangman_assets/gap.xcf').convert_alpha()
            gap_rect = gap_place.get_rect(center = ((i*60) + 250,275))
            window.blit(gap_place,gap_rect)

def over_button():
    mouse_pos = pygame.mouse.get_pos()
    over_button = False
    for button in buttons:
        if button.collidepoint(mouse_pos):
            over_button = True

    return over_button

def return_letter_pressed():
    mouse_pos = pygame.mouse.get_pos()
    for button_pair in buttons_and_letters:
        if button_pair[0].collidepoint(mouse_pos):
            return button_pair[0],button_pair[1],button_pair

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and over_button():
                button,letter,button_pair = return_letter_pressed()
                button_letters.remove(letter)
                buttons.remove(button)
        
        window.fill(WHITE)
        draw_buttons(button_letters)
        make_gaps()
        over_button()
        pygame.display.update()
        clock.tick(FPS)

run()
