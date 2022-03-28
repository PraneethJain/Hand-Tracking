import requests
import numpy as np
import imutils
import cv2
from settings import *


def get_image():
    url = "http://192.168.1.37:8080/shot.jpg"
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=WIDTH, height=HEIGHT)
    return img
