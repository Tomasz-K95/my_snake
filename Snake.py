import pygame

running = True

def launching_the_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    while running:
        rysowanie_tla(screen)
        obsluga_zdarzeń()
        pygame.display.flip()
    pygame.quit()

def obsluga_zdarzeń():
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


def rysowanie_tla(screen):
    return screen.fill((10,100,30))

launching_the_game()