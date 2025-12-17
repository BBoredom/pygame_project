import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Empty groups to be created before game loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add Player class before the player object instance is created
    Player.containers = (updatable, drawable)

    # add Asteroids class to asteroids, updatable and drawable
    Asteroid.containers = (asteroids, updatable, drawable)

    # set containers for Shot class to new group like with Plater and Asteroid Class
    Shot.containers = (shots, updatable, drawable)

    # add AsteroidField class to updatable group as it is not drawable (make it a tuple by ending with a comma)
    AsteroidField.containers = (updatable, )

    # Create AsteroidField object
    asteroidfield = AsteroidField()

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
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # limiting the framerate to 60 FPS
        dt = clock.tick(60) / 1000


# keep everything below this at the bottom of the file
if __name__ == "__main__":
    main()
