import sys
from PIL import Image, ImageQt, ImageDraw
from PyQt5.Qt import *
from PyQt5 import uic
from PIL.ImageQt import ImageQt
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.creat.clicked.connect(self.crt)

    def crt(self):
        im = Image.new('RGB', (260, 260), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        r = random.randint(50, 250)
        draw.ellipse((50, 50, r, r), fill=(255, 255, 0))

        im.save('res.jpg', quality=95)
        self.current_image = Image.open('res.jpg')
        self.img_qt = ImageQt(self.current_image)
        self.pixmap = QPixmap.fromImage(self.img_qt)
        self.image.setPixmap(self.pixmap)
        

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())