import pygame
import random

running = True
klawisze = {pygame.K_w : (0,-20),
                pygame.K_s : (0, 20),
                pygame.K_a : (-20, 0),
                pygame.K_d : (20 , 0)}

def launching_the_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    snake = [(180, 150), (200, 150), (220, 150), (240,150), (260, 150)]
    kierunek = (0, 20)
    jabko = losuj_jablka(snake)
    spowolnienie_gry = pygame.time.Clock()

    while running:
        rysowanie_tla(screen)
        kierunek = obsluga_zdarzen(kierunek)
        ruch_weza(snake, kierunek)
        rysowanie_weza(screen, snake)
        spowolnienie_gry.tick(6)
        pygame.display.flip()
    pygame.quit()


def obsluga_zdarzen(kierunek: tuple) -> tuple:
    global running

    nowy_kierunek = kierunek
    user_input = pygame.event.get()
    for event in user_input:
        if event.type == pygame.KEYDOWN:
            # zdefiniowany został słownik z kalwiszami i kierunkami żeby uprościć zapis i sprawdzenie czy nie zachodzi zwrot o 180 st.
            if event.key in klawisze:
                przeciwny = czy_przeciwny(kierunek, klawisze[event.key])
                if not przeciwny:
                    nowy_kierunek = klawisze[event.key]
        if event.type == pygame.QUIT:
            running = False
            break
    kierunek = nowy_kierunek
    return kierunek


def rysowanie_tla(screen) -> None:
    screen.fill((0, 0, 0))


def rysowanie_weza(screen, snake: list[tuple]) -> None:
    for x, y in snake:
        pygame.draw.rect(screen, (0, 200, 0), (x, y, 20, 20))


def ruch_weza(snake: list[tuple], kierunek: tuple) -> None:
    x, y = snake[-1]  # glowa weza
    zmiana_x, zmiana_y = kierunek
    ruch = (x + zmiana_x, y + zmiana_y)
    snake.append(ruch)
    snake.pop(0)

def czy_przeciwny(kierunek1: tuple, kierunek2: tuple) -> bool:
    k1_x , k1_y = kierunek1
    k2_x, k2_y = kierunek2
    if k1_x == -k2_x and k1_y == -k2_y:
        return True
    else:
        return False

def losuj_jablka(snake:list[tuple]) -> None:

    jabko_x = random.randrange(20, 600, 20)
    jabko_y = random.randrange(20, 600, 20)
    jabko = (jabko_x,jabko_y)
    for elem in snake:
        if jabko == elem:
            jabko_x = random.randrange(20, 600, 20)
            jabko_y = random.randrange(20, 600, 20)
    return jabko

launching_the_game()
