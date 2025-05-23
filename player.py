from constants import *
from circleshape import *

class Shot(CircleShape):
	def __init__(self,x,y,rotation):
		super().__init__(x,y,SHOT_RADIUS)
		self.rotation = rotation

	def draw(self, screen):
		pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SHOT_SPEED * dt

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x,y,PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0
	# in the player class
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)

	def update(self, dt):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_a]:
			self.rotate((-1 * dt))
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move((-1 * dt))
		if keys[pygame.K_SPACE]:
			self.shoot()
		self.timer -= dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.timer > 0:
			return
		bullet = Shot(self.position.x, self.position.y, self.rotation)
		self.timer = SHOT_COOLDOWN
