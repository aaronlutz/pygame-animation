import pygame
import math


class Slider:
	
	def __init__(self, settings):
		# horizontal slider, 1 y value, 2 x values
		# vertical slider, 2 y values, 1 x value
		
		# need to flip the x and y's

		# Bar
		self.perc_screen = settings.slider_perc_screen
		self.y = settings.slider_y
		self.bar_color = settings.slider_line_color
		# Handle
		self.handle_color = settings.slider_handle_color
		self.handle_width = settings.slider_handle_width
		self.handle_height = settings.slider_handle_height
		
		
		self.set_line_points(settings)
		# Mouse
		self.clicked = False
		# Output Value
		self.max_value = settings.slider_max_value
		self.min_value = settings.slider_min_value
		self.value = settings.slider_start_value 
		
		self.bar = self.Bar(self, settings)
		self.handle = self.Handle(self.bar, settings)
		
	class Bar:
		
		def __init__(self, slider, settings):
			# Position
			screen_width = settings.screen_width
			self.length = screen_width * slider.perc_screen
			self.left = (screen_width / 2 - self.bar_length / 2, slider.y)
			self.right = (screen_width / 2 + self.bar_length / 2, slider.y)
			
	class Handle:
		
		def __init__(self, bar, settings):
			# Position

			self.perc = settings.slider_start_value / (settings.slider_min_value - settings.slider_max_value)
			self.x = self.right_x - (bar.length * self.perc)
			self.top = (self.x, self.y + self.handle_height / 2)
			self.bot = (self.x, self.y - self.handle_height / 2)


	def check_if_clicked(self, event_pos):
		mouse_x = event_pos[0]
		mouse_y = event_pos[1]

		h_top_y = self.handle_y - self.h_height/2
		h_bot_y = self.handle_y + self.h_height/2
		h_lef_x = self.x - self.h_width 
		h_rig_x = self.x + self.h_width

		
		if h_lef_x <= mouse_x and mouse_x <= h_rig_x:
			if h_top_y <= mouse_y and mouse_y <= h_bot_y:
				self.clicked = True
		print(str(self.clicked) + '\n')		
		
	
	def update_slider(self, event_pos):
		
		if self.clicked:
			print('slider def update_slider')
			mouse_y = event_pos[1]
			if self.top_y <= mouse_y and mouse_y <= self.bot_y:
				self.handle_y = mouse_y
				self.left = (self.h_left_x, self.handle_y)
				self.right = (self.h_right_x, self.handle_y)

				position_perc = 1 - ((self.handle_y - self.top[1]) / self.slider_height) 
				value_range = self.min_value - self.max_value

				self.value = int(value_range * position_perc)

		
	def draw_me(self, screen):
		pygame.draw.line(screen, self.lcolor, self.top, self.bottom)
		pygame.draw.line(screen, self.hcolor, self.left, self.right, self.h_height)
		
