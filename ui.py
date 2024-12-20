from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import sys

def start_ui(simulation_env):
    app = QApplication(sys.argv)
    window = QMainWindow()
    label = QLabel("Simulation Running...", parent=window)
    window.setCentralWidget(label)
    window.setWindowTitle("Pedestrian Simulation")
    window.show()
    sys.exit(app.exec_())
