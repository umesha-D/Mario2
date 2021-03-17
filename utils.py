import pygame

def load_image(image_name):
    return pygame.image.load("./img/" + image_name)

def load_sound(sound_name):
    return pygame.mixer.Sound("./sound/" + sound_name)