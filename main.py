import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Empty groups to be created before game loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add Player class before the player object instance is created
    Player.containers = (updatable, drawable)

    # Player position
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # limiting the framerate to 60 FPS
        dt = clock.tick(60) / 1000


# keep everything below this at the bottom of the file
if __name__ == "__main__":
    main()
