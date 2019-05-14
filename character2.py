import os
import pygame


class Character():
    def __init__(self, settings):
        self.images = []
        # Image Size
        self.width = 100
        self.height = 100
        self.dim = (self.width, self.height)
        self.settings = settings
        # Animations
        self.stand_left = self.load_from_file(
            '\\Users\\aaron\\Documents\\python_work\\Animating\\standing\\standing_left.bmp')
        self.stand_right = self.load_from_file(
            '\\Users\\aaron\\Documents\\python_work\\Animating\\standing\\standing_right.bmp')
        self.kneel_left = self.load_from_file(
            '\\Users\\aaron\\Documents\\python_work\\Animating\\kneel\\kneel_left.bmp')
        self.kneel_right = self.load_from_file(
            '\\Users\\aaron\\Documents\\python_work\\Animating\\kneel\\kneel_right.bmp')
        self.walk_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\walking_left\\')
        self.walk_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\walking_right\\')
        self.jump_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\jump_right\\')
        self.jump_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\jump_left\\')
        self.backflip_right = self.load_from_folder(
            '\\Users\\aaron\\Documents\\python_work\\Animating\\backflip_right\\')
        self.backflip_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\backflip_left\\')
        self.climb_right = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\climbing_right\\')
        self.climb_left = self.load_from_folder('\\Users\\aaron\\Documents\\python_work\\Animating\\climbing_left\\')
        # Direction Indicators
        self.direction = 'right'
        self.action = 'standing'

        # Current Frame
        self.frame = 0
        self.frame_total = 0
        self.jump_frame_start = 0
        self.max_frame = 0
        # Image Location
        self.x = settings.screen_width / 2  # GetSystemMetrics(0) / 2
        self.y = 175 + 200 - self.height
        self.delta_x = 0
        self.delta_y = 0
        self.pos = (self.x, self.y)
        self.frame = 0
        self.vertical_coef = 1

    def load_from_folder(self, folder_path):
        temp_image_list = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".bmp"):
                image = pygame.image.load(folder_path + file_name)
                image = pygame.transform.scale(image, self.dim)
                image = image.convert()
                image.set_colorkey(self.settings.transparent_color)
                temp_image_list.append(image)
        return temp_image_list


    def load_from_file(self, file_path):
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, self.dim)
        image = image.convert()
        image.set_colorkey(self.settings.transparent_color)
        return image

    def set_action(self, action):
        wait_actions = ['jumping', 'backflipping']

        if not self.action in wait_actions:
            # print('old action: ' + str(self.action) + ' frame: ' + str(self.frame) + ' new action: ' + str(action))
            self.action = action
            if action in wait_actions:
                self.frame = 0

        else:
            print(action + ' denied because he is ' + self.action + ' frame[' + str(self.frame) + ']')

    def do(self, scene):
        # print(self.y)
        action = self.action
        if action == 'standing':
            self.stand()
        elif action == 'kneeling':
            self.kneel()
        elif action == 'walking':
            self.walk()
        elif action == 'jumping':
            self.jump()
        elif action == 'backflipping':
            self.backflip()
        elif action == 'climbing':
            self.climb()
        self.update_location(scene)
        self.frame_total += 1

    def stand(self):
        print('def stand')
        self.delta_x = 0
        self.delta_y = 0
        self.max_frame = 0
        if self.direction == 'right':
            self.image = self.stand_right
        elif self.direction == 'left':
            self.image = self.stand_left

    def kneel(self):
        print('def kneel')
        self.delta_x = 0
        self.delta_y = 0
        self.max_frame = 0
        if self.direction == 'right':
            self.image = self.kneel_right
        elif self.direction == 'left':
            self.image = self.kneel_left

    def walk(self):
        print('def walk')
        self.delta_y = 0
        self.max_frame = len(self.walk_right) - 1
        if self.direction == 'right':
            self.delta_x = 10
            self.image = self.walk_right[self.frame]
        elif self.direction == 'left':
            self.delta_x = -10
            self.image = self.walk_left[self.frame]

    def jump(self):
        print('def jump')
        # Delta XY per Frame
        self.jump_x_increments = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.jump_y_increments = [0, 0, -15, -35, 0, 35, 15, 0, 0]
        self.max_frame = len(self.jump_right) - 1
        # Set Delta XY
        self.delta_x = self.jump_x_increments[self.frame]
        self.delta_y = self.jump_y_increments[self.frame]
        # Set Image
        if self.direction == 'right':
            self.image = self.jump_right[self.frame]
        elif self.direction == 'left':
            self.image = self.jump_left[self.frame]
        # Terminate Action
        if self.frame == len(self.jump_right) - 1:
            self.action = 'standing'

    def backflip(self):
        print('def backflip')
        self.backflip_x_increments = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.backflip_y_increments = [0, 0, -15, -30, 0, 0, 30, 15, 0, 0, 0]
        self.max_frame = len(self.backflip_right) - 1
        # Set Delta XY
        self.delta_x = self.backflip_x_increments[self.frame]
        self.delta_y = self.backflip_y_increments[self.frame]
        # Set Image
        if self.direction == 'right':
            self.image = self.backflip_right[self.frame]
        elif self.direction == 'left':
            self.image = self.backflip_left[self.frame]
        # Terminate Action
        if self.frame == len(self.backflip_right) - 1:
            self.action = 'standing'

    def climb(self):
        print('def climb')
        self.climb_x_increments = [0, 0, 0, 0, 0, 0, 0, 0]
        self.climb_y_increments = [-3, -3, -3, -3, -3, -3, -3, -3]
        self.max_frame = len(self.climb_right) - 1
        # Set Delta XY
        self.delta_x = self.climb_x_increments[self.frame]
        self.delta_y = self.climb_y_increments[self.frame] * self.vertical_coef
        # Set Image
        if self.direction == 'right':
            self.image = self.climb_right[self.frame]
        elif self.direction == 'left':
            self.image = self.climb_left[self.frame]

    def update_location(self, scene):
        scene.increment_x(self.delta_x, self.frame_total)
        self.y += self.delta_y
        self.pos = (self.x, self.y)

    def increment_frame(self):
        #		if self.frame == self.max_frame:
        #			self.action = 'standing'
        if self.frame < self.max_frame:
            self.frame += 1
        else:
            self.frame = 0

    def blitme(self, screen):
        screen.blit(self.image, self.pos)
