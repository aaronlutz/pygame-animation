
class Settings():
	def __init__(self):
		
		# Screen
		self.screen_width = 1500
		self.screen_height = 400
		self.screen_dim = (self.screen_width, self.screen_height)
		
		# Character
		self.char_start_y = 175
		
		# Images
		self.transparent_color = (255, 0, 255)
		
		# Delay Display
		self.dd_pos = (20,20)
		# Frame Display
		self.fd_pos = (self.dd_pos[0], self.dd_pos[1] + 20)
		# Character XY Display
		self.xy_pos = (self.screen_width - 100, 20)
		# Character Delta XY Display
		self.delta_xy_pos = (self.screen_width - 100, self.xy_pos[1] + 20)
		# Character Action Display
		self.action_pos = (self.screen_width/2, 20)
		# Character Direction Display
		self.direction_pos = (self.screen_width/2, self.action_pos[1] + 20)
		# Delta Y since start
		self.delta_y_pos = (self.screen_width - 100, self.delta_xy_pos[1] + 20)
		
		# Slider
		self.slider_perc_screen = 0.5
		self.slider_x = 20
		self.slider_line_color = (212,212,212)
		self.slider_handle_color = (30, 144, 255)
		self.slider_handle_width = 30
		self.slider_handle_height = 15
		self.slider_max_value = 0
		self.slider_min_value = 1000
		self.slider_start_value = 100
		
		# Ground
		self.ground_color = (43, 185, 109)
		self.ground_height = 25
		
