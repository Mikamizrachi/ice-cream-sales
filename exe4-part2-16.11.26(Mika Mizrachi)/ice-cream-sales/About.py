from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap


class About(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 400)
        self.setWindowTitle("About Me")
        self.setStyleSheet("background-color: lightcoral")

        self.name = QLabel("Mika Mizrachi", self)
        self.name.setGeometry(120, 20, 250, 30)
        self.name.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.email = QLabel("📩: 555mika555@gmail.com", self)
        self.email.setGeometry(70, 280, 250, 30)
        self.email.setStyleSheet("font-size: 14px; font-family : 'Segoe UI Emoji'")

        self.linkedin = QLabel('🔗<a href="https://www.linkedin.com/in/mika-mizrachi-85b733433/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BHofLLhiwRfOI0SZ16sG%2FPA%3D%3D">  My LinkedIn</a>', self)
        self.linkedin.setGeometry(70, 320, 250, 30)
        self.linkedin.setStyleSheet("font-size: 14px;")
        self.linkedin.setOpenExternalLinks(True)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(75, 60, 200, 200)
        self.my_picture.setStyleSheet("border : 4px solid white ; border-radius : 10px")
        image = QPixmap("mika.jpg").scaled(200, 200)
        self.my_picture.setPixmap(image)

        self.github = QLabel('🐙<a href="https://github.com/Mikamizrachi">  My GitHub</a>', self)
        self.github.setGeometry(70, 360, 250, 30)
        self.github.setStyleSheet("font-size: 14px;")
        self.github.setOpenExternalLinks(True)


if __name__ == "__main__":
    app = QApplication()
    window = About()
    window.show()
    app.exec()
