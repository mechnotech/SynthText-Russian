# Author: Ankush Gupta
# Date: 2015
"""Script to generate font-models."""

import pickle

import numpy as np
import pygame
from pygame import freetype

from text_utils import FontState

pygame.init()

ys = np.arange(8, 200)
A = np.c_[ys, np.ones_like(ys)]

xs = []
models = {}  # linear model

FS = FontState()

for i in range(len(FS.fonts)):
    print(i, FS.fonts[i])
    font = freetype.Font(FS.fonts[i], size=12)
    h = []
    for y in ys:
        h.append(font.get_sized_glyph_height(float(y)))
    h = np.array(h)
    m, _, _, _ = np.linalg.lstsq(A, h, rcond=None)
    models[font.name] = m
    xs.append(h)

with open('data/models/font_px2pt.cp', 'wb') as f:
    pickle.dump(obj=models, file=f)
