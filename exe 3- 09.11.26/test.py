from PySide6.QtWidgets import QApplication, QWidget

app = QApplication()
window = QWidget()
window.setGeometry(100,100,500,500)
window.setWindowTitle('Hey Mika')


window.show()
app.exec()