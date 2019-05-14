import time
import math
import pygame.font

class Label():
	
	def __init__(self, left_x, top_y, screen, msg, txt_color, bg_color, height, width):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# get coordinates
		x = left_x
		y = top_y
		
		
		# Set the dimension and properties of the button
		self.side_length = 800 / 80
		self.width = width
		self.height = height
		self.button_color = bg_color
		self.text_color = txt_color
		self.font = pygame.font.SysFont(None, 30)
		
		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.left = self.x
		self.rect.top = self.y
		
		# The button message needs to be prepped only once
		self.prep_msg(msg)
		self.draw_button()
	
	
	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(str(msg), True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		# Draw blank button and then draw message
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class GameClock():
	def __init__(self, screen, pos, txt_color=(0,0,0), font_size=100):
		'''Metric Displayed Onscreen'''
		# Screen
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# Font
		self.font = pygame.font.SysFont(None, font_size)
		self.text_color = txt_color
		# Dimension

		self.pos = pos
		# Build the button's rect object and center it.
		
		# First Image
		txt = '0 S'
		self.image = self.font.render(txt, True, (0,0,0))
		self.image_rect = self.image.get_rect()
		self.rect = pygame.Rect(0, 0, self.image_rect.width, self.image_rect.height)
		self.rect.center = (pos[0] - self.image_rect.width, pos[1] - self.image_rect.height)
		self.image_rect.center = self.rect.center
		
	def start_clock(self):
		'''Begin Game Clock.'''
		self.start_time = time.time()
		self.now_time = int(time.time())
		self.prev_elap_time = self.now_time - self.start_time
		
	def update(self):
		'''Update Value Displayed OnScreen'''
		self.now_time = time.time()
		if self.sufficient_elapse():
			msg = self.format_seconds()
			self.image = self.font.render(msg, True, (0,0,0))
			self.image_rect = self.image.get_rect()
			self.image_rect.center = self.rect.center

	def sufficient_elapse(self):
		'''Prevent a Timer from being rendered every frame.'''
		elap_time = self.now_time - self.start_time
		if elap_time > int(self.prev_elap_time) + 1:
			self.prev_elap_time = elap_time
			return True
		else:
			return False
				
	def format_seconds(self):
		'''format seconds into minutes seconds.'''
		elap_seconds = time.time() - self.start_time 
		if elap_seconds <= 60:
			elap_txt = str(int(elap_seconds)) + ' S'
		else:
			elap_min = int(elap_seconds / 60)
			elap_sec = (elap_seconds % 60)
			elap_txt = str(elap_min) + ' M ' + str(int(elap_sec)) + ' S'
		return elap_txt

	def blitme(self):
		'''Draw Value to Screen.'''
		self.screen.blit(self.image,self.image_rect)





	
class ReadOut():
	
	def __init__(self, screen, pos, val, txt_color=(0,0,0), font_size=100, pre_text='', post_text='', clock=False):
		'''Metric Displayed Onscreen'''
		# Screen
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# Font
		self.font = pygame.font.SysFont(None, font_size)
		self.text_color = txt_color
		# Dimension
		self.show = True
		self.pos = pos
		# Build the button's rect object and center it.
		self.pre_text = pre_text
		self.post_text = post_text
		self.update_val(val)
		
	def update_val(self, new_value):
		'''Update Value Displayed OnScreen'''
		self.val = self.pre_text + str(new_value) + self.post_text
		self.image = self.font.render(str(self.val), True, self.text_color)
		self.image_rect = self.image.get_rect()
		self.rect = pygame.Rect(0, 0, self.image_rect.width, self.image_rect.height)
		#print(self.image_rect.width, self.image_rect.height)
		self.rect.left = self.pos[0]
		self.rect.top =  self.pos[1] #(self.pos[0] - self.image_rect.width, self.pos[1] - self.image_rect.height)
		self.image_rect.left = self.pos[0]
		self.image_rect.top = self.pos[1]
		

	def blitme(self):
		'''Draw Value to Screen.'''
		if self.show:
			self.screen.blit(self.image,self.image_rect)
		

