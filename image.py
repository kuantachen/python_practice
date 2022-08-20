from PIL import Image
import os


for file in os.listdir('orig'):
    if file.endswith('.jpg'):
        image_file = Image.open(os.path.join('orig', file))    # open color image
        image_file = image_file.convert('L')    # covert image to black and white
        image_file.save(os.path.join('result', file[:-4] + '_grey.png'))
