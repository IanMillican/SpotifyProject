import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from SpotifyRecap import getNumListensPerSong

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.numListensPerSong = None

        # Set window properties
        self.setWindowTitle("My Own Spotify Wrapped")

        # Create Widgets
        self.label = QLabel("Testing Loading data")
        self.loadButton = QPushButton("Click here to load files")
        self.loadButton.clicked.connect(self.load)  # Connect button click to method
        self.mostListenedButton = QPushButton("Click here for most listened to song")
        self.mostListenedButton.clicked.connect(self.mostListened)

        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Enter the path to the folder containing your Spotify data...")
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.loadButton)
        layout.addWidget(self.textbox)
        layout.addWidget(self.mostListenedButton)

        # Set layout
        self.setLayout(layout)

    def load(self):
        folderPath = self.textbox.text()
        self.numListensPerSong = getNumListensPerSong(folderPath)
        if self.numListensPerSong is None:
            self.label.setText("Error: No \".json\" files found")
        elif len(self.numListensPerSong.items())>0:
            self.label.setText("Successfully loaded the spotify data")
        else:
            self.label.setText("Error: Unknown issue occured")
    def mostListened(self):
        if self.numListensPerSong is None:
            self.label.setText("Make sure to load the data first")
        else:
            mostListens = ""
            currMax = 0
            for key, val in self.numListensPerSong.items():
                if val > currMax:
                    mostListens = key
                    currMax = val
            self.label.setText(f"The most listened to song in the last 10 years is {mostListens}\n and it was listened to {currMax} times")

# Run the Application
app = QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec())
