# This util is just used for Display purpose
import cv2
from matplotlib import pyplot as plt


images = [cv2.cvtColor(cv2.imread('grouped_workers.png'), cv2.COLOR_BGR2RGB), 
          cv2.cvtColor(cv2.imread('web_services.png'), cv2.COLOR_BGR2RGB)]
image_names = ['grouped_workers', 'web_services']


def display(images, image_names, fig_zize):
    num_images = len(images) # Maximum number of images to display
    num_cols = 2 # Number of columns in display
    num_rows = num_images//num_cols # Number of rows in display
    plt.figure(figsize=(fig_zize*2, fig_zize*num_cols))
    for i in range(num_rows*num_cols):

        plt.subplot(num_rows, num_cols, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(image_names[i], size=12)
        plt.axis('off') 