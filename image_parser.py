import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

def crop(image, coords, saved_location):
    ''' crops and saves the given image '''

    # crop the larger spritesheet into unoptimized sections
    cropped_image = image.crop(coords)
    cropped_image.save('{}.{}'.format(saved_location,'png'))

def rotate(saved_location, degree):
    ''' opens, rotates, and saves the image '''

    img_file = Image.open('{}.{}'.format(saved_location,'png'))
    rot_img = img_file.rotate(degree)
    rot_img.save('{}.{}'.format(saved_location,'png'))
    

def optimize(saved_location): 
    ''' optimizes the image by removing whitespace '''
  
    # reopen section and analyze pixel data
    img_file = Image.open('{}.{}'.format(saved_location,'png'))
    img = img_file.load()
    [xs, ys] = img_file.size
    x1,y1,x2,y2 = xs,ys,0,0

    # (3) Examine each pixel in the image file
    for y in range(0, ys):
      for x in range(0, xs):
        # (4)  Get the RGB color of the pixel
        if img[x, y] != (0,0,0,0):
          if y1 > y:
            y1 = y
          if y2 < y:
            y2 = y
          if x1 > x:
            x1 = x
          if x2 < x:
            x2 = x

    coords = (x1,y1,x2,y2)

    crop(img_file, coords, saved_location)

def crop_spritesheet(spritesheet, cols, rows):
  ''' creates cropped groups of images removing unessesary whitespace'''

  # open the image
  im = Image.open('{}.png'.format(spritesheet))

  # total number of cells and width / height
  total = cols * rows                
  w = im.size[0]/cols
  h = im.size[1]/rows

  cellindex = 0

  # for each cell, create a new optimized image in the
  # format IMAGE_cellindex.png
  for row in range(rows):
    for col in range(cols):
        cell = (col * w,row * h,(col+1) * w, (row+1) * h)
        crop(im, cell, '{}_{}'.format(spritesheet, cellindex))
        optimize('{}_{}'.format(spritesheet, cellindex))
        cellindex += 1


image = 'fire_collide'
cols = 5
rows = 4
crop_spritesheet(image, cols, rows)


