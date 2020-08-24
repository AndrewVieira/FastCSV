#python3 -m venv venv
#call venv/scripts/activate.bat
#pip install PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    table = QTableWidget(100, 100)
    layout.addWidget(table)
    window.show()
    app.exec_()

