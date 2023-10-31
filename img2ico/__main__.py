import sys
from PySide6 import QtWidgets

from img2ico.gui import Window


def main():
    app = QtWidgets.QApplication([])

    window = Window()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
