import numpy as np
import tensorflow as tf
from skimage.color import rgb2lab, lab2rgb

IMG_SIZE = 256

def preprocess_image(image):
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    image = tf.cast(image, tf.float32) / 255.0
    return image

def rgb_to_l(image):
    lab = rgb2lab(image)
    L = lab[..., :1] / 100.0
    return L, lab

def reconstruct_rgb(L, AB):
    lab = np.concatenate([L * 100.0, AB * 128.0], axis=-1)
    rgb = lab2rgb(lab)
    return (rgb * 255).astype(np.uint8)
