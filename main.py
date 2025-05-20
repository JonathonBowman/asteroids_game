import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	Clock = pygame.time.Clock()
	dt = 0
	# (before doesn't work)player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Shot.containers = (updatable, drawable, shots)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		updatable.update(dt)
		for rock in asteroids:
			if rock.collision_check(player):
				print("Game over!")
				return
		for rock in asteroids:
			for bullet in shots:
				if rock.collision_check(bullet):
					rock.split()
					bullet.kill()
		screen.fill((0,0,0))
		for pic in drawable:
			pic.draw(screen)
		#player.draw(screen)
		pygame.display.flip()
		x = Clock.tick(60) / 1000
		dt = x

if __name__ == "__main__":
	main()

