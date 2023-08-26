import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, collision_sprites):
		super().__init__(groups)

		self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
		self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(topleft=pos)
        
        # player movement
		self.direction = pygame.math.Vector2()
		self.speed = 4
		self.gravity = 0.4
		self.jump_speed = 10
		self.collision_sprites = collision_sprites
		self.on_floor = False
        
	def input(self):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0
			
		if (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_floor:
			self.direction.y = -self.jump_speed
			
	def horizontal_collision(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left
			
	def vertical_collision(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0
		
		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y
			
	def update(self):
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collision()
		self.apply_gravity()
		self.vertical_collision()
