import pygame


def launching_the_game():
    pygame.init()

    screen = pygame.display.set_mode((600, 800))
    rysowanie_tla(screen)
    running = True
    while running:
        pass
    pygame.display.flip()

def obsluga_zdarzeń():
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
        if event.type == pygame.quit():
            running = False


def rysowanie_tla(screen):
    return screen.fill((10,20,30))