import os
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from PIL import Image, ImageOps
import numpy as np
from tqdm import tqdm
import argparse
import shutil
import sys
import argparse

# output size
WIDTH = 200
HEIGHT = 200

# add noize on RGB
noise_std = 20


parser = argparse.ArgumentParser(description='Create colored mnist dataset.')
parser.add_argument('--output_path',default='.', type=str,
                    help='Name for dataset path.')
parser.add_argument('--output_label', default='number', type=str,
                    help='You can choose output label (number or color).')

args = parser.parse_args()
output_path = args.output_path
output_label = args.output_label

if not os.path.exists(output_path + '/train'):
    os.mkdir(output_path + '/train')

if not os.path.exists(output_path + '/test'):
    os.mkdir(output_path + '/test')

# mnist load
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# define color list
color_lst = {}
color_lst['blue'] = [0,0,255]
color_lst['yellow'] = [255,255,0]
color_lst['red'] = [255,0,0]
color_lst['purple'] = [128,0,128]
color_lst['green'] = [0,128,0]

len_color = len(color_lst)
for i in tqdm(range(10)):
    train_inx = np.where(y_train == i)[0]
    np.random.seed(seed = 32)
    np.random.shuffle(train_inx)
    len_train = len(train_inx) // len_color

    test_inx = np.where(y_test == i)[0]
    np.random.seed(seed = 32)
    np.random.shuffle(test_inx)
    len_test = len(test_inx) // len_color
    for j, color in enumerate(color_lst):
        if output_label == 'color':
            out_path = color
        elif output_label == 'number':
            out_path = str(i)
        else:
            print('output_label must be color or number')
            sys.exist()
        if not os.path.exists(output_path + '/train/' + out_path):
            os.mkdir(output_path + '/train/' + out_path)
        if not os.path.exists(output_path + '/test/' + out_path):
            os.mkdir(output_path + '/test/' + out_path)

        c_train_inx = train_inx[j*len_train:(j+1)*len_train]
        c_test_inx = test_inx[j*len_test:(j+1)*len_test]
        c_train = x_train[c_train_inx]
        for k in range(len_train):
            img = Image.fromarray(c_train[k])
            rgb = color_lst[color] + np.random.normal(0, noise_std, 3)
            rgb = np.where(rgb <= 255, rgb, 255)
            rgb = np.where(rgb >= 0, rgb, 0)
            color_img = ImageOps.colorize(img, black=(0, 0, 0), white=rgb).resize((WIDTH,HEIGHT))
            color_img.save(f'{output_path}/train/{out_path}/{i}_{color}_{k}.jpg')

        c_test_inx = test_inx[j*len_test:(j+1)*len_test]
        c_test_inx = test_inx[j*len_test:(j+1)*len_test]
        c_test = x_test[c_test_inx]
        for k in range(len_test):
            img = Image.fromarray(c_test[k])
            rgb = color_lst[color] + np.random.normal(0, noise_std, 3)
            rgb = np.where(rgb <= 255, rgb, 255)
            rgb = np.where(rgb >= 0, rgb, 0)
            color_img = ImageOps.colorize(img, black=(0, 0, 0), white=rgb).resize((WIDTH,HEIGHT))
            color_img.save(f'{output_path}/test/{out_path}/{i}_{color}_{k}.jpg')
            