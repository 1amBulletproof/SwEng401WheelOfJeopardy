import sys
from PyQt4 import QtGui, QtCore
import random

class WheelView(object):
    def __init__(self, graphics_view):
        self.MAX_EXTRA_ROTATIONS = 4

        self.view = graphics_view

        self.wheel_pixmap = QtGui.QPixmap('wheelofjeopardy/wheel.png')
        self.scene = QtGui.QGraphicsScene(self.view)
        self.item = QtGui.QGraphicsPixmapItem(self.wheel_pixmap)
        self.scene.addItem(self.item)
        self.view.setScene(self.scene)

        self.current_location = 0
        self.on_finished = None

        self.sector_locations = {
            "bankrupt":   0,   "category1":         30,  "free spin":       60,
            "category2":  90,  "lose turn":         120, "category3":       150,
            "spin again": 180, "category4":         210, "player's choice": 240,
            "category5":  270, "opponent's choice": 300, "category6":       330
        }

    def spin_to_sector(self, sector_name):
        print "Spinning to sector: %s" % sector_name
        self.tl = QtCore.QTimeLine(5000)
        self.tl.setFrameRange(0, 100)
        self.tl.setEasingCurve(QtCore.QEasingCurve.InOutCubic)  # InOutQuart
        self.tl.setDirection(QtCore.QTimeLine.Forward)

        self.animation = QtGui.QGraphicsItemAnimation()
        self.animation.setItem(self.item)
        self.animation.setTimeLine(self.tl)
        self.animation.setTranslationAt(0, self.wheel_pixmap.width() / -2, self.wheel_pixmap.height() / -2)
        self.animation.setPosAt(0, QtCore.QPointF(self.wheel_pixmap.width() / 2, self.wheel_pixmap.height() / 2))
        self.animation.setRotationAt(0, self.current_location)
        self.current_location = -self.sector_locations[sector_name]
        extra_rotations = random.randrange(2, self.MAX_EXTRA_ROTATIONS, 1)
        self.animation.setRotationAt(1, self.current_location - (360 * extra_rotations))

        if self.on_finished != None:
            self.tl.finished.connect(self.on_finished)

        self.tl.start()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    view = WheelView()
    view.setMinimumSize(600, 600)
    view.show()
    view.spin()
    sys.exit(app.exec_())
