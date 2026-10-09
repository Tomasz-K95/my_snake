import pygame

running = True

def launching_the_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    snake = [(180,150),(200,150),(220,150)]
    spowolnienie_gry = pygame.time.Clock()


    while running:
        rysowanie_tla(screen)
        obsluga_zdarzeń()
        ruch_weza(snake)
        rysowanie_weza(screen, snake)
        spowolnienie_gry.tick(2)
        pygame.display.flip()
    pygame.quit()

def obsluga_zdarzeń() -> None:
    global running
    user_input = pygame.event.get()
    for event in user_input:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            elif event.key == pygame.K_s:
                pass
            elif event.key == pygame.K_a:
                pass
            elif event.key == pygame.K_d:
                pass
        if event.type == pygame.QUIT:
            running = False
            break


def rysowanie_tla(screen) -> None:
    screen.fill((0,0,0))

def rysowanie_weza(screen, snake: list[tuple]) -> None:
    for x,y in snake:
        pygame.draw.rect(screen,(0,200,0), (x,y,20,20))


def ruch_weza(snake: list[tuple]):
    x, y = snake[-1]  # glowa weza
    ruch =  (x+20, y)
    snake.append(ruch)
    snake.pop(0)


launching_the_game()