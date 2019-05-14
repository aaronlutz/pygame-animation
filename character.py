import os
import pygame

class Character():
	def __init__(self, settings):
		self.images = []
		# Image Size
		self.width = 200
		self.height = 200
		self.dim = (self.width, self.height)

		# Animations
		self.stand_left = self.load_from_file('\\Users\\aaron\\Documents\\python_work\\Animating\\standing\\standing_left.bmp')
		self.stand_right = self.load_from_file('\\Users\\aaron\\Documents\\python_work\\Animating\\standing\\standing_right.bmp')
		self.kneel_left = self.load_from_file('\\Users\\aaron\\Documents\\python_work\\Animating\\kneel\\kneel_left.bmp')
		self.kneel_right = self.load_from_file('\\Users\\aaron\\Documents\\python_work\\Animating\\kneel\\kneel_right.bmp')
		self.walk_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\walking_left\\')
		self.walk_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\walking_right\\')
		self.jump_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\jump_right\\')
		self.jump_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\jump_left\\')
		self.backflip_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\backflip_right\\')
		self.backflip_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\backflip_left\\')
		# Direction Indicators
		self.direction = 'right'
		
		self.walking = False
		self.jumping = False
		self.backflipping = False
		self.kneeling = False
		# Current Frame 
		self.frame = 0
		self.frame_total = 0
		self.jump_frame_start = 0
		self.current_max_frame = 0 # some animations are longer than others, the frame loops needs to start over at different times
		# Image Location
		self.x = 0 #  GetSystemMetrics(0) / 2
		self.y = settings.char_start_y
		self.delta_x = 0
		self.delta_y = 0
		self.pos = (self.x, self.y)
		self.frame = 0
		
	def load_from_folder(self, folder_path):
		temp_image_list = []
		for file_name in os.listdir(folder_path):
			if file_name.endswith(".bmp"):
				image = pygame.image.load(folder_path + file_name)
				image = pygame.transform.scale(image, self.dim)	
				temp_image_list.append(image)
		return temp_image_list
	
	def load_from_file(self, file_path):
		image = pygame.image.load(file_path)
		image = pygame.transform.scale(image, self.dim)	
		return image		
				
	def blitme(self, screen):
		screen.blit(self.image, self.pos)
	
	def kneel(self):
		if not self.jumping:
			self.walking = False
			self.kneeling = True
	
	def backflip(self):
		if not self.jumping:
			if not self.backflipping:
				self.backflipping = True
				self.kneeling = False
				self.jump_frame_start = self.frame_total
				self.current_max_frame = len(self.backflip_right) - 1
				self.frame = 0
				
	def jump(self):
		if not self.jumping:
			self.jumping = True
			self.kneeling = False
			self.jump_frame_start = self.frame_total
			self.current_max_frame = len(self.jump_right) - 1
			self.frame = 0
	
	def update_location(self):
		walk_increment = 20
		jump_increment = 5
		if self.walking:
			if self.direction == 'right':
				self.delta_x = walk_increment
				self.x += walk_increment
			if self.direction == 'left':
				self.delta_x = -1*walk_increment
				self.x -= walk_increment
		if self.jumping:
			#print('jumping: ' + str(self.jumping))
			jump_increments = [0, 0, -15, -35, 0, 35, 15, 0, 0]
			self.delta_y = jump_increments[self.frame]
			self.y += jump_increments[self.frame]
			if self.frame == 7:
				self.jumping = False
		if self.backflipping:
			#print('jumping: ' + str(self.jumping))
			jump_increments = [0, 0, -15, -35, 0, 0, 0, 35, 25, 0, 0]
			self.delta_y = jump_increments[self.frame]
			self.y += jump_increments[self.frame]	
			if self.frame == 13:
				self.backflipping = False				
			
		self.pos = (self.x, self.y)
	
	def update_image(self):
		#print(self.frame)
		if self.jumping:
			if self.direction == 'right':
				self.image = self.jump_right[self.frame]
			elif self.direction == 'left':
				self.image = self.jump_left[self.frame]
		elif self.backflipping:
			if self.direction == 'right':
				self.image = self.backflip_right[self.frame]
			elif self.direction == 'left':
				self.image = self.backflip_left[self.frame]			
		elif self.walking:
			if self.direction == 'right':
				self.image = self.walk_right[self.frame]
			elif self.direction == 'left':
				self.image = self.walk_left[self.frame]
		elif self.kneeling:
			if self.direction == 'right':
				self.image = self.kneel_right
			elif self.direction == 'left':
				self.image = self.kneel_left
		else:
			if self.direction == 'right':
				self.image = self.stand_right
			elif self.direction == 'left':
				self.image = self.stand_left
				
	def increment_frame(self):
		if self.frame == self.current_max_frame:
			if self.jumping:
				self.jumping = False
			elif self.backflipping:
				self.backflipping = False				
		#if not self.jumping and not self.backflipping:
		
		
		#print('increment_frame, self.current_max_frame = ' + str(self.current_max_frame))
		if self.frame < self.current_max_frame:
			self.frame += 1
		else:
			self.frame = 0
		#print('increment_frame, self.frame = ' + str(self.frame))
#		else:
#			self.frame += 1
