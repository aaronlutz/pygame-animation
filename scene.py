import pygame
import os
import time


class Scene():
    def __init__(self, screen, settings):
        # Tree
        self.tree_dim = (int(280 * 1.75), int(210 * 1.75))
        self.tree = self.load_from_file(settings,
                                        '\\Users\\aaron\\Documents\\python_work\\Animating\\background\\tree.bmp')
        self.tree_x = settings.screen_width * 0.55
        self.tree_y = settings.screen_height - settings.ground_height - self.tree_dim[1]
        self.tree_pos = (self.tree_x, self.tree_y)
        # Clouds
        self.cloud_increment_count = 1
        self.cloud_scale = 5
        self.clouds = self.load_from_folder(settings,
                                            '\\Users\\aaron\\Documents\\python_work\\Animating\\background\\clouds\\',
                                            scale=self.cloud_scale)
        self.cloud_poss = [(settings.screen_width * 0.1, 100), (settings.screen_width * 0.4, 75),
                           (settings.screen_width * 0.65, 60)]
        self.start_time = start_time = time.time()

    def draw_clouds(self, screen):
        for x in range(0, len(self.clouds)):
            pos = self.cloud_poss[x]
            screen.blit(self.clouds[x], pos)

    def increment_x(self, delta_x, frame_total):
        self.tree_x -= delta_x
        self.tree_pos = (self.tree_x, self.tree_y)

    def increment_clouds(self):
        now_time = time.time()
        if now_time - self.start_time > 1:
            for x in range(0, len(self.cloud_poss)):
                new_dim = (self.cloud_poss[x][0] + 5, self.cloud_poss[x][1])
                self.cloud_poss[x] = new_dim
                self.cloud_increment_count += 1
            self.start_time = time.time()

    def draw_scene(self, screen, settings):
        top = settings.screen_height - settings.ground_height
        ground_rect = pygame.Rect(0, top, settings.screen_width, settings.ground_height)
        pygame.draw.rect(screen, settings.ground_color, ground_rect)
        self.increment_clouds()
        self.draw_clouds(screen)
        screen.blit(self.tree, self.tree_pos)

    def load_from_folder(self, settings, folder_path, scale=1):
        temp_image_list = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".bmp"):
                image = pygame.image.load(folder_path + file_name)

                image = image.convert()
                image.set_colorkey(settings.transparent_color)
                image_dim = image.get_rect().size
                new_dim = (image_dim[0] * scale, image_dim[1] * scale)
                image = pygame.transform.scale(image, new_dim)
                temp_image_list.append(image)
        return temp_image_list

    def load_from_file(self, settings, file_path):
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, self.tree_dim)
        image = image.convert()
        image.set_colorkey(settings.transparent_color)
        return image
