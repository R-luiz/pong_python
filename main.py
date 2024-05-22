# pong game using pygame library

import pygame
import random
import time

# initialize pygame
class Ball:
	def __init__(self):
		self.x = 300
		self.y = 200
		self.radius = 8
		self.color = (255, 255, 255)
		self.speed_x = 3.5 * random.choice((1, -1))
		self.speed_y = 3.5 * random.choice((1, -1))
		self.player1_points = 0
		self.player2_points = 0
	
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
	def move(self):
		self.x += self.speed_x
		self.y += self.speed_y
		if self.y <= 0 or self.y >= 400:
			self.speed_y *= -1
		if self.x <= 0 or self.x >= 600:
			if self.x <= 0:
				self.player2_points += 1
			else:
				self.player1_points += 1
			self.x = 300
			self.y = 200
			self.speed_x = 3 * random.choice((1, -1))
			self.speed_y = 3 * random.choice((1, -1))
	def collision(self, pad1, pad2):
		if self.x - self.radius <= pad1.x + pad1.width and pad1.y <= self.y <= pad1.y + pad1.height:
			self.speed_x *= -1.2

		if self.x + self.radius >= pad2.x and pad2.y <= self.y <= pad2.y + pad2.height:
			self.speed_x *= -1.2

class Paddle:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 5
		self.height = 60
		self.color = (255, 255, 255)
		self.speed = 5
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
	def move_up(self):
		self.y -= self.speed
		if self.y <= 0:
			self.y = 0
	def move_down(self):
		self.y += self.speed
		if self.y >= 350:
			self.y = 350

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pong Game")

# create objects
ball = Ball()
pad1 = Paddle(5, 175)
pad2 = Paddle(590, 175)

# game loop
running = True

while running:
	screen.fill((0, 0, 0))
	# print points
	font = pygame.font.Font(None, 36)
	text = font.render(str(ball.player1_points), True, (255, 255, 255))
	screen.blit(text, (250, 10))
	text = font.render(str(ball.player2_points), True, (255, 255, 255))
	screen.blit(text, (330, 10))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		pad1.move_up()
	if keys[pygame.K_s]:
		pad1.move_down()
	if keys[pygame.K_UP]:
		pad2.move_up()
	if keys[pygame.K_DOWN]:
		pad2.move_down()
	if ball.player1_points == 10 or ball.player2_points == 10:
		running = False
	if keys[pygame.K_ESCAPE]:
		running = False
	ball.move()
	ball.collision(pad1, pad2)
	pad1.speed = abs(ball.speed_x) * 1.2
	pad2.speed = abs(ball.speed_x) * 1.2
	ball.draw(screen)
	pad1.draw(screen)
	pad2.draw(screen)
	pygame.display.flip()
	time.sleep(0.01)
pygame.quit()