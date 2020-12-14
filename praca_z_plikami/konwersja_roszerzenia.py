from PIL import Image
import os

picture_1 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_1.jpg'))
picture_1.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_1_conv.png'))

picture_2 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_2.jpg'))
picture_2.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_2_conv.png'))

picture_3 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_3.jpg'))
picture_3.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_3_conv.png'))

picture_4 = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_4.jpg'))
picture_4.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'picture_4_conv.png'))
