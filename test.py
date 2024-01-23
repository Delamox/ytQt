import sys
from PyQt6 import QtCore, QtGui, QtW

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()
        self.videoslider.setGeometry(QtCore.QRect(10, 730, 1260, 20))
        self.videoslider.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "border: 1px solid #74cbfc;\n"
                                       "background: #2b2b2b;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::sub-page:horizontal {\n"
                                       "background: #2b2b2b;\n"
                                       "border: 1px solid #e974fc;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::add-page:horizontal {\n"
                                       "background: #2b2b2b;\n"
                                       "border: 1px solid #74cbfc;\n"
                                       "height: 10px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "background: #4d4d4d;\n"
                                       "border: 1px solid #4d4d4d;\n"
                                       "width: 13px;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal:hover {\n"
                                       "background: #a8a8a8;\n"
                                       "border: 1px solid #a8a8a8;\n"
                                       "border-radius: 4px;\n"
                                       "}\n"
                                       "")
        self.videoslider.setMinimum(1)
        self.videoslider.setMaximum(1000)
        self.videoslider.setSingleStep(10)
        self.videoslider.setPageStep(1)
        self.videoslider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.videoslider.setInvertedControls(False)
        self.videoslider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.videoslider.setTickInterval(1)
        self.videoslider.setObjectName("videoslider")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()