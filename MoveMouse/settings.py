import pygame as pg

pg.init()
WIDTH, HEIGHT = 1280, 720
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Phone camera")
ORIGIN = (0, 0)
SCALE_FACTOR = 1.5  # 1920/1280 = 1080/720 = 1.5
