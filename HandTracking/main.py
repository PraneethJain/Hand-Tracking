import cv2
import pygame as pg
import numpy as np
from rich import print
from cvzone.HandTrackingModule import HandDetector
from settings import *
from image import *


def cv_to_pg(img: np.array) -> pg.Surface:
    """Converts opencv image into pygame image

    Args:
        img (np.array): cv2 image

    Returns:
        pg.Surface: pygame image
    """
    return pg.transform.flip(
        pg.image.frombuffer(img.tobytes(), img.shape[1::-1], "BGR"), True, False
    )


def mp_to_pg(pos: tuple[int, int]) -> tuple[int, int]:
    """Convert mediapipe coordinates to pygame coordinates

    Args:
        pos (tuple[int, int]): mediapipe/cvzone coordinates

    Returns:
        tuple[int, int]: pygame coordinates
    """
    return (WIDTH - pos[0], pos[1])


def handleEvents(events):
    for event in events:
        if event.type == pg.QUIT:
            raise SystemExit
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                raise SystemExit


detector = HandDetector()
to_draw = set()
while True:

    handleEvents(pg.event.get())

    img = get_image()
    img = cv2.resize(img, (WIDTH, HEIGHT))
    hands, img = detector.findHands(img)
    frame = cv_to_pg(img)

    screen.blit(frame, ORIGIN)
    if hands:
        if all(
            all(hand["lmList"][i + 3][1] > hand["lmList"][i][1] for i in (5, 9, 13, 17))
            for hand in hands
        ):
            raise SystemExit
        for hand in hands:
            if (
                all(
                    hand["lmList"][i + 3][1] > hand["lmList"][i][1] for i in (9, 13, 17)
                )
                and hand["lmList"][8][1] < hand["lmList"][5][1]
            ):
                to_draw.add(mp_to_pg(tuple(hand["lmList"][8][0:2])))
            if all(
                hand["lmList"][i + 3][1] > hand["lmList"][i][1] for i in (5, 9, 13, 17)
            ):
                to_draw = set()

    for drawing in to_draw:
        pg.draw.circle(screen, "black", drawing, 10, 0)

    pg.display.flip()
