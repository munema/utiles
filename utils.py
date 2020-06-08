from PIL import Image, ImageDraw, ImageFilter, ImageOps
import os
import numpy as np
import pathlib
import shutil
import numpy as np
import sys

# change extention
def change_suffix(file_name, to_suffix = '.png'):
    st = pathlib.PurePath(file_name).stem
    parent = str(pathlib.Path(file_name).parent)
    to_name = parent + '/' + st + to_suffix
    shutil.move(file_name, to_name)

# crop original image based on mask image
def crop_base_mask_img(original_img_path, mask_image_path):
    src = np.array(Image.open(original_img_path))
    mask = np.array(Image.open(mask_image_path))
    mask = mask / 255 # 0 or 1
    mask = mask.astype(np.uint8) # int 0 ~ 255
    dst = src.copy()
    if len(src.shape) == 2:
        dst *= mask
    else:
        dst[:,:,0] *= mask
        dst[:,:,1] *= mask
        dst[:,:,2] *= mask
    img = Image.fromarray(dst.astype(np.uint8))
    return img


# change color
# RGB → HSV → change color operation (base on color angle(H) and param min_sv (SV)) → RGB
def change_color_img(img_path, color, min_sv = 0.5, color_noise = True):
    img = Image.open(img_path)
    h, s, v = img.convert("HSV").split()
    p = min_sv
    color_dct = {}
    color_dct['blue'] = {}
    color_dct['blue']['angle'] = 240
    color_dct['blue']['range'] = 25
    color_dct['yellow'] = {}
    color_dct['yellow']['angle'] = 60
    color_dct['yellow']['range'] = 15
    color_dct['red'] = {}
    color_dct['red']['angle'] = 0
    color_dct['red']['range'] = 10
    color_dct['green'] = {}
    color_dct['green']['angle'] = 120
    color_dct['green']['range'] = 30

    color_name_lst = list(color_dct.keys())
    if color not in color_name_lst:
        color
        print(r'Color Selection ERROR : You can choose {color_name_lst}')
        sys.exit()

    color_p = color_dct[color]['angle']
    lower = color_p - color_dct[color]['range']
    # fix lower because red color's lower is minus
    if lower < 0:
        lower += 360
    higher = color_p + color_dct[color]['range']

    if color_noise:
        color_p = np.random.normal(color_p, color_dct[color]['range']/2)
        if color_p < 0:
        color_p += 360
        elif color_p > 360:
        color_p -= 360

    # nomalization [0,360]→[0,255]
    color_p *= 255/360
    higher *= 255/360
    lower *= 255/360

    img_colored = Image.merge(
        "HSV",
        (
            h.point(lambda x: x if (x > lower and x < higher) else color_p),
            s.point(lambda x: max(x,int(p*255))),
            v.point(lambda x: max(x,int(p*255)))
        )
    ).convert("RGB")

    return img_colored
