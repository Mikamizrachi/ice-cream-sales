import sys, os, csv
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from About import About
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []

        self.setWindowTitle("Ice Cream Sales")

        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("aboutBtn")
        self.about_btn.setFixedWidth(80)
        self.about_btn.clicked.connect(self.show_about)

        self.open_btn = QPushButton("Choose File")
        self.open_btn.setObjectName("chooseBtn")
        self.open_btn.setFixedWidth(250)
        self.open_btn.clicked.connect(self.load_file)


        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.ax = self.figure.add_subplot(111)


        top_row = QHBoxLayout()
        top_row.addWidget(self.about_btn)
        top_row.addStretch()

        choose_row = QHBoxLayout()
        choose_row.addStretch()
        choose_row.addWidget(self.open_btn)
        choose_row.addStretch()

        layout = QVBoxLayout(self)
        layout.addLayout(top_row)
        layout.addLayout(choose_row)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)




    def show_about(self):
        self.about = About()
        self.about.show()


    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose file", "", "CSV Files (*.csv)")
        if not file_name:
            return

        self.temperatures.clear()
        self.revenues.clear()
        with open(file_name, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            next(reader)                     
            for row in reader:
                self.temperatures.append(float(row[0]))
                self.revenues.append(float(row[1]))

        self.plot_graph()   

    def plot_graph(self):
        self.ax.clear()                  

        self.ax.scatter(self.temperatures, self.revenues, s=1)

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_title("Ice Cream Revenue vs. Temperature")
        self.ax.set_xlabel("Temperature (°C)")
        self.ax.set_ylabel("Revenue ($)")

        self.canvas.draw()                     


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qss_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    with open(qss_path, encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    window = IceCreamWindow()
    window.resize(800, 650)
    window.show()
    sys.exit(app.exec())
