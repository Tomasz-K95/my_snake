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
    snake = [(180, 140), (200, 140), (220, 140), (240,140), (260, 140)]
    kierunek = (0, 20)
    jabko = losuj_jablka(snake)
    spowolnienie_gry = pygame.time.Clock()
    game_over = False


    while running:
        rysowanie_tla(screen)
        kierunek = obsluga_zdarzen(kierunek)
        ruch_weza(snake, kierunek)
        rysowanie_weza(screen, snake)
        jabko = jedzenie_jabka(snake, jabko)
        rysowanie_jabka(screen,jabko)
        game_over = sciana_i_waz(snake)
        pygame.display.flip()
        spowolnienie_gry.tick(5)
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

def losuj_jablka(snake:list[tuple]) -> tuple:

    jabko_x = random.randrange(20, 600, 20)
    jabko_y = random.randrange(20, 600, 20)
    jabko = (jabko_x,jabko_y)
    while jabko in snake:
        jabko_x = random.randrange(20, 600, 20)
        jabko_y = random.randrange(20, 600, 20)
        jabko = (jabko_x, jabko_y)
    return jabko

def rysowanie_jabka(screen,jabko: tuple) -> None:
    x, y = jabko
    pygame.draw.circle(screen, (250, 0, 0), (x+10, y+10), 10)

def jedzenie_jabka(snake, jabko) -> tuple:
    if snake[-1] == jabko:
        snake.insert(0, snake[0])
        jabko = losuj_jablka(snake)
    return jabko


def sciana_i_waz(snake):
    x, y = snake[-1]
    game_over = False
    if x > 599 or y > 599:
        game_over = True
    if x < 0 or y < 0:
        game_over = True
    else:
        for segment in snake[:-1]:
            snake_x, snake_y = segment
            if x == snake_x and y == snake_y:
                game_over = True
    return game_over

launching_the_game()
