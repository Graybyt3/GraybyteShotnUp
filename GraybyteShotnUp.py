#!/usr/bin/env python3
import sys
import os
import requests
import subprocess
import time
import uuid
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QComboBox, QInputDialog, QMessageBox,
                             QSystemTrayIcon, QMenu, QStatusBar, QLabel, QDesktopWidget, QSpacerItem,
                             QSizePolicy, QCheckBox, QDialog, QFrame)
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage, QIcon, QFont, QColor, QMovie
from PyQt5.QtCore import Qt, QPoint, QRect, QTimer, QPropertyAnimation, QEasingCurve
from PIL import Image
import tempfile
import configparser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Graybyt3 - Ex-Blackhat 🖤 | Ex Super Mod of Team_CC.
# Now securing systems as a Senior Security Expert 🛡️.
# I hack servers for fun, patch them to torture you.
#
# "My life is a lie, and i'm living in this only truth.- Graybyt3"
#
# WARNING: Steal my code, and I'll call you Pappu
# There's no worse shame in this world than being called Pappu.
# FuCk_Pappu

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(SCRIPT_DIR, "config-log")
ICONS_DIR = os.path.join(SCRIPT_DIR, "icons")

os.makedirs(CONFIG_DIR, exist_ok=True)
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.ini")

class AboutMeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Graybyt3")
        self.setFixedSize(600, 400)
        self.setStyleSheet("""
            QDialog {
                background-color: rgba(20, 20, 30, 0.7);
                border: 1px solid #404050;
                border-radius: 8px;
            }
            QLabel {
                color: #b0c4de;
                font: 12pt "Roboto";
                font-weight: bold;
            }
            QPushButton {
                background-color: #404050;
                color: #b0c4de;
                border: none;
                padding: 6px 10px;
                border-radius: 6px;
                font: bold 12pt "Roboto";
            }
            QPushButton:hover {
                background-color: #3366cc;
                color: #ffffff;
            }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        content = QLabel("""
            <p style='text-align: center; color: #ff3333; font: 18pt "Roboto"; font-weight: bold; text-decoration: underline;'>
                Graybyt3
            </p>
            <p style='text-align: center; color: #b0c4de; font: 14pt "Roboto"; font-weight: bold;'>
                🖤 Ex-Blackhat<br>
                🎩 Ex Super Mod of Team_CC | 🛡️ Senior Security Expert<br>
                💻 I hack servers for fun, patch them to torture you. 😈
            </p>
        """)
        content.setAlignment(Qt.AlignCenter)
        layout.addWidget(content)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        self.center_on_parent()

    def center_on_parent(self):
        if self.parent():
            parent_geometry = self.parent().geometry()
            dialog_geometry = self.geometry()
            x = parent_geometry.x() + (parent_geometry.width() - dialog_geometry.width()) // 2
            y = parent_geometry.y() + (parent_geometry.height() - dialog_geometry.height()) // 2
            self.move(x, y)

class ContactMeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Contact Graybyt3")
        self.setFixedSize(600, 400)
        self.setStyleSheet("""
            QDialog {
                background-color: rgba(20, 20, 30, 0.7);
                border: 1px solid #404050;
                border-radius: 8px;
            }
            QLabel {
                color: #b0c4de;
                font: 15pt "Roboto";
                font-weight: bold;
            }
            QPushButton {
                background-color: #404050;
                color: #b0c4de;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font: bold 12pt "Roboto";
            }
            QPushButton:hover {
                background-color: #3366cc;
                color: #ffffff;
            }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)
        icons_widget = QWidget()
        icons_layout = QHBoxLayout(icons_widget)
        icons_layout.setAlignment(Qt.AlignCenter)

        def create_icon_label(icon_filename, link):
            icon_path = os.path.join(ICONS_DIR, icon_filename)
            label = QLabel()
            pixmap = QPixmap()
            try:
                if not os.path.exists(icon_path):
                    raise FileNotFoundError(f"Icon file not found: {icon_path}")
                pixmap.load(icon_path)
                if pixmap.isNull():
                    raise ValueError("Failed to load icon")
                pixmap = pixmap.scaled(65, 65, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                label.setPixmap(pixmap)
            except Exception as e:
                label.setText("Icon load failed")
                print(f"Failed to load icon from {icon_path}: {e}")
            label.setAlignment(Qt.AlignCenter)
            label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            label.setOpenExternalLinks(True)
            label.setText(f"<a href='{link}'><img src='file://{icon_path}' width='64' height='64'></a>")
            return label

        github_label = create_icon_label("git.png", "https://github.com/Graybyt3")
        telegram_label = create_icon_label("tele.png", "https://t.me/rex_cc")
        facebook_label = create_icon_label("fb.png", "https://www.facebook.com/graybyt3")
        instagram_label = create_icon_label("insta.png", "https://www.instagram.com/gray_byte")
        x_label = create_icon_label("twi.png", "https://x.com/gray_byte")
        icons_layout.addWidget(github_label)
        icons_layout.addWidget(telegram_label)
        icons_layout.addWidget(facebook_label)
        icons_layout.addWidget(instagram_label)
        icons_layout.addWidget(x_label)
        layout.addWidget(icons_widget)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        self.center_on_parent()

    def center_on_parent(self):
        if self.parent():
            parent_geometry = self.parent().geometry()
            dialog_geometry = self.geometry()
            x = parent_geometry.x() + (parent_geometry.width() - dialog_geometry.width()) // 2
            y = parent_geometry.y() + (parent_geometry.height() - dialog_geometry.height()) // 2
            self.move(x, y)

class NotificationWidget(QWidget):
    def __init__(self, message, url=None, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.6)
        self.url = url
        self.setFixedSize(500, 200)
        self.movie = None

        layout = QHBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        self.gif_label = QLabel(self)
        self.gif_label.setFixedSize(100, 100)
        self.gif_label.setAlignment(Qt.AlignCenter)
        gif_path = os.path.join(ICONS_DIR, "ok.gif")
        if os.path.exists(gif_path):
            self.movie = QMovie(gif_path)
            self.movie.setScaledSize(self.gif_label.size())
            self.gif_label.setMovie(self.movie)
            self.movie.start()
        else:
            self.gif_label.setText("GIF not found")
            self.gif_label.setStyleSheet("color: #ff3333; font: 10pt 'Roboto';")
        layout.addWidget(self.gif_label)

        text_layout = QVBoxLayout()
        self.label = QLabel(message, self)
        self.label.setFont(QFont("Roboto", 12, QFont.Bold))
        self.label.setWordWrap(True)
        self.label.setStyleSheet("""
            background-color: transparent;
            color: #ffffff;
            font: 13pt "Roboto";
            font-weight: bold;
        """)
        text_layout.addWidget(self.label, alignment=Qt.AlignTop)

        if url:
            self.url_button = QPushButton("Open URL", self)
            self.url_button.setStyleSheet("""
                background-color: #404050;
                color: #b0c4de;
                border: 1px solid #3366cc;
                padding: 8px;
                border-radius: 5px;
                font: bold 12pt "Roboto";
            """)
            self.url_button.clicked.connect(self.open_url)
            text_layout.addWidget(self.url_button, alignment=Qt.AlignBottom)
        text_layout.addStretch()
        layout.addLayout(text_layout)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e1e2a, stop:1 #2a2a3a);
                border: 2px double #3366cc;
                border-radius: 12px;
            }
        """)

        screen = QDesktopWidget().screenGeometry()
        self.move(screen.width() - 500 - 30, screen.height() - 200 - 40)

        self.opacity = QPropertyAnimation(self, b"windowOpacity")
        self.opacity.setDuration(10000)
        self.opacity.setStartValue(1.0)
        self.opacity.setEndValue(0.0)
        self.opacity.setEasingCurve(QEasingCurve.InOutQuad)
        self.opacity.finished.connect(self.on_animation_finished)

        self.close_timer = QTimer(self)
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(self.close)

    def on_animation_finished(self):
        if self.movie:
            self.movie.stop()
        self.close()

    def update_message(self, message, url=None):
        self.label.setText(message)
        self.url = url
        if url and not hasattr(self, 'url_button'):
            self.url_button = QPushButton("Open URL", self)
            self.url_button.setStyleSheet("""
                background-color: #404050;
                color: #b0c4de;
                border: 1px solid #3366cc;
                padding: 8px;
                border-radius: 5px;
                font: bold 12pt "Roboto";
            """)
            self.url_button.clicked.connect(self.open_url)
            self.layout().itemAt(1).layout().insertWidget(1, self.url_button, alignment=Qt.AlignBottom)
        elif not url and hasattr(self, 'url_button'):
            self.url_button.deleteLater()
            del self.url_button
            self.layout().itemAt(1).layout().addStretch()
        screen = QDesktopWidget().screenGeometry()
        self.move(screen.width() - 500 - 30, screen.height() - 200 - 30)
        if "Speed" in message:
            if self.movie:
                self.movie.start()
            self.opacity.start()
            self.close_timer.start(5500)

    def open_url(self):
        if self.url:
            webbrowser.open(self.url)

    def show(self):
        super().show()
        self.raise_()
        if self.movie:
            self.movie.start()

class GraybyteImageUploader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GRAYBYTE-SHOT n UP | DOUBLE TROUBLE API")
        self.setWindowOpacity(0.85)
        self.drawing = False
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.pixmap = None
        self.current_tool = "rectangle"
        self.shapes = []
        self.gyazo_api_key = ""
        self.imgur_client_id = ""
        self.use_imgur = True
        self.use_gyazo = True
        self.load_config()
        self.notification = None
        # Set window icon dynamically
        self.setWindowIcon(QIcon(os.path.join(ICONS_DIR, "icon.png")))
        self.init_ui()
        self.create_menu_bar()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.init_tray()
        self.clear_canvas()
        self.update_preview()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: rgba(20, 20, 30, 0.8);
                color: #b0c4de;
                font: bold 12pt "Roboto";
            }
            QMenuBar::item {
                background: transparent;
                color: #b0c4de;
            }
            QMenuBar::item:selected {
                background: #404050;
                color: #ffffff;
            }
            QMenu {
                background-color: rgba(20, 20, 30, 0.8);
                color: #b0c4de;
                border: 1px solid #404050;
            }
            QMenu::item:selected {
                background-color: #3366cc;
                color: #ffffff;
            }
        """)
        file_menu = menu_bar.addMenu("File")
        capture_action = QMenu("Capture", self)
        capture_action.addAction("New Capture", self.start_capture)
        save_action = file_menu.addAction("Save Locally", self.save_locally)
        clear_action = file_menu.addAction("Clear Canvas", self.clear_canvas)
        api_action = file_menu.addAction("Set API Keys", self.set_api_keys)
        exit_action = file_menu.addAction("Exit", QApplication.quit)
        file_menu.addAction(capture_action.menuAction())
        file_menu.addAction(save_action)
        file_menu.addAction(clear_action)
        file_menu.addAction(api_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        tools_menu = menu_bar.addMenu("Tools")
        upload_action = tools_menu.addAction("Upload Image", self.upload_image)
        about_menu = menu_bar.addAction("About", self.show_about_dialog)
        aboutme_menu = menu_bar.addAction("AboutMe", self.show_aboutme_dialog)
        contactme_menu = menu_bar.addAction("ContactMe", self.show_contactme_dialog)
        docs_menu = menu_bar.addAction("Documentation", lambda: webbrowser.open("https://github.com/Graybyt3"))

    def show_about_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("About GRAYBYTE - SHOT n UP")
        dialog.setFixedSize(500, 250)
        dialog.setStyleSheet("""
            QDialog {
                background-color: rgba(20, 20, 30, 0.7);
                border: 1px solid #404050;
                border-radius: 8px;
            }
            QLabel {
                color: #b0c4de;
                font: 12pt "Roboto";
                font-weight: bold;
            }
            QPushButton {
                background-color: #404050;
                color: #b0c4de;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font: bold 12pt "Roboto";
            }
            QPushButton:hover {
                background-color: #3366cc;
                color: #ffffff;
            }
        """)
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        content = QLabel("""
            <p style='text-align: center; color: #b0c4de; font: 14pt "Roboto";'>
                GraybyteImageUploader - Version 1.0<br><br>
                Built to simplify and enhance<br>
                screenshot capture and upload on Linux.
            </p>
        """)
        content.setAlignment(Qt.AlignCenter)
        layout.addWidget(content)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        dialog.move(
            self.geometry().x() + (self.geometry().width() - dialog.width()) // 2,
            self.geometry().y() + (self.geometry().height() - dialog.height()) // 2
        )
        dialog.exec_()

    def show_aboutme_dialog(self):
        dialog = AboutMeDialog(self)
        dialog.exec_()

    def show_contactme_dialog(self):
        dialog = ContactMeDialog(self)
        dialog.exec_()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)
        self.preview_label = QLabel(self)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setFixedSize(1140, 590)
        self.preview_label.setStyleSheet("background-color: transparent;")
        main_layout.addWidget(self.preview_label, alignment=Qt.AlignCenter)
        api_container = QWidget()
        api_layout = QHBoxLayout(api_container)
        api_layout.setSpacing(20)
        api_layout.setContentsMargins(0, 10, 0, 10)
        self.imgur_check = QCheckBox("Use Imgur")
        self.imgur_check.setChecked(self.use_imgur)
        self.imgur_check.stateChanged.connect(self.update_api_preference)
        self.imgur_check.setStyleSheet("color: #FFFFFF; font-size: 14px;")
        api_layout.addWidget(self.imgur_check)
        self.gyazo_check = QCheckBox("Use Gyazo")
        self.gyazo_check.setChecked(self.use_gyazo)
        self.gyazo_check.stateChanged.connect(self.update_api_preference)
        self.gyazo_check.setStyleSheet("color: #FFFFFF; font-size: 14px;")
        api_layout.addWidget(self.gyazo_check)
        main_layout.addWidget(api_container, alignment=Qt.AlignCenter)
        toolbar = QHBoxLayout()
        toolbar.setSpacing(10)
        toolbar.setAlignment(Qt.AlignCenter)
        self.tool_combo = QComboBox()
        self.tool_combo.addItems(["Line", "Freehand", "Rectangle", "Circle", "Arrow", "Text"])
        self.tool_combo.setCurrentText("Rectangle")
        self.tool_combo.currentTextChanged.connect(self.set_tool)
        self.tool_combo.setStyleSheet("""
            padding: 8px;
            font-size: 14px;
            border-radius: 5px;
            background-color: #2E2E2E;
            color: white;
            border: 1px solid #555555;
        """)
        self.tool_combo.setFixedWidth(120)
        toolbar.addWidget(self.tool_combo)
        aboutme_btn = QPushButton("AboutMe")
        aboutme_btn.clicked.connect(self.show_aboutme_dialog)
        aboutme_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #4CAF50;
            color: white;
            border: none;
        """)
        toolbar.addWidget(aboutme_btn)
        capture_btn = QPushButton("Capture")
        capture_btn.clicked.connect(self.start_capture)
        capture_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #2196F3;
            color: white;
            border: none;
        """)
        toolbar.addWidget(capture_btn)
        upload_btn = QPushButton("Upload")
        upload_btn.clicked.connect(self.upload_image)
        upload_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #9C27B0;
            color: white;
            border: none;
        """)
        toolbar.addWidget(upload_btn)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_locally)
        save_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #FF9800;
            color: white;
            border: none;
        """)
        toolbar.addWidget(save_btn)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear_canvas)
        clear_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #F44336;
            color: white;
            border: none;
        """)
        toolbar.addWidget(clear_btn)
        api_key_btn = QPushButton("Set API Keys")
        api_key_btn.clicked.connect(self.set_api_keys)
        api_key_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #607D8B;
            color: white;
            border: none;
        """)
        toolbar.addWidget(api_key_btn)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #D32F2F;
            color: white;
            border: none;
        """)
        toolbar.addWidget(close_btn)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(toolbar)
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QWidget {
                color: #FFFFFF;
                font-family: Roboto, sans-serif;
            }
            QPushButton {
                background-color: #333333;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 6px;
                font-size: 14px;
                min-width: 80px;
            }
            QComboBox {
                background-color: #2E2E2E;
                color: white;
                border: 1px solid #555555;
                padding: 8px;
                border-radius: 5px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QStatusBar {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
        """)

    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon(os.path.join(ICONS_DIR, "icon.png")), self)
        tray_menu = QMenu()
        capture_action = tray_menu.addAction("Capture")
        capture_action.triggered.connect(self.start_capture)
        open_action = tray_menu.addAction("Open")
        open_action.triggered.connect(self.open_with_clear_canvas)
        config_action = tray_menu.addAction("Set API Keys")
        config_action.triggered.connect(self.set_api_keys)
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(QApplication.quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.start_capture()
        elif reason == QSystemTrayIcon.Context:
            self.open_with_clear_canvas()

    def open_with_clear_canvas(self):
        self.clear_canvas()
        self.show()

    def show(self):
        super().show()
        self.update_preview()

    def load_config(self):
        config = configparser.ConfigParser()
        if os.path.exists(CONFIG_FILE):
            config.read(CONFIG_FILE)
            self.gyazo_api_key = config.get("General", "gyazo_api_key", fallback="")
            self.imgur_client_id = config.get("General", "imgur_client_id", fallback="")
            self.use_imgur = config.getboolean("General", "use_imgur", fallback=True)
            self.use_gyazo = config.getboolean("General", "use_gyazo", fallback=True)
        else:
            self.save_config()

    def save_config(self):
        config = configparser.ConfigParser()
        config["General"] = {
            "gyazo_api_key": self.gyazo_api_key,
            "imgur_client_id": self.imgur_client_id,
            "use_imgur": str(self.use_imgur),
            "use_gyazo": str(self.use_gyazo)
        }
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            config.write(f)
        os.chmod(CONFIG_FILE, 0o600)

    def update_api_preference(self):
        self.use_imgur = self.imgur_check.isChecked()
        self.use_gyazo = self.gyazo_check.isChecked()
        self.save_config()
        self.show_message("Success", "API preferences updated.", QMessageBox.Information)

    def set_api_keys(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Gyazo API Key")
        dialog.setLabelText("Enter your Gyazo API Key:")
        dialog.setTextValue(self.gyazo_api_key)
        dialog.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")
        screen = QDesktopWidget().screenGeometry()
        dialog.move(screen.width() - dialog.width() - 20, screen.height() - dialog.height() - 20)
        if dialog.exec_() == QInputDialog.Accepted:
            self.gyazo_api_key = dialog.textValue()

        dialog = QInputDialog(self)
        dialog.setWindowTitle("Imgur Client-ID")
        dialog.setLabelText("Enter your Imgur Client-ID:")
        dialog.setTextValue(self.imgur_client_id)
        dialog.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")
        dialog.move(screen.width() - dialog.width() - 20, screen.height() - dialog.height() - 20)
        if dialog.exec_() == QInputDialog.Accepted:
            self.imgur_client_id = dialog.textValue()

        if self.gyazo_api_key or self.imgur_client_id:
            self.save_config()
            self.show_message("Success", "API Keys saved.", QMessageBox.Information)

    def show_message(self, title, message, icon):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")
        screen = QDesktopWidget().screenGeometry()
        msg.move(screen.width() - msg.width() - 20, screen.height() - msg.height() - 20)
        msg.exec_()

    def set_tool(self, tool):
        self.current_tool = tool.lower()
        self.status_bar.showMessage(f"Tool: {tool}")

    def start_capture(self):
        self.status_bar.showMessage("Capturing...")
        self.hide()
        if subprocess.run(["which", "scrot"], capture_output=True).returncode != 0:
            self.show_message("Error", "scrot is not installed. Please install it (e.g., 'sudo apt install scrot' or 'sudo pacman -S scrot').", QMessageBox.Critical)
            self.show()
            self.status_bar.showMessage("Ready")
            return
        temp_file = os.path.join(tempfile.gettempdir(), f"graybyte_screenshot_{uuid.uuid4().hex}.png")
        try:
            result = subprocess.run(["scrot", "-s", temp_file], capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                self.show_message("Error", f"Failed to capture screenshot: {result.stderr}", QMessageBox.Critical)
                self.show()
                self.status_bar.showMessage("Ready")
                return
        except subprocess.TimeoutExpired:
            self.show_message("Error", "Screenshot capture timed out.", QMessageBox.Critical)
            self.show()
            self.status_bar.showMessage("Ready")
            return
        except Exception as e:
            self.show_message("Error", f"Unexpected error during capture: {str(e)}", QMessageBox.Critical)
            self.show()
            self.status_bar.showMessage("Ready")
            return
        if not os.path.exists(temp_file):
            self.show_message("Error", "Failed to capture screenshot.", QMessageBox.Critical)
            self.show()
            self.status_bar.showMessage("Ready")
            return
        self.pixmap = QPixmap(temp_file)
        if self.pixmap.isNull():
            self.show_message("Error", "Failed to load screenshot.", QMessageBox.Critical)
            self.pixmap = None
            if os.path.exists(temp_file):
                os.unlink(temp_file)
            self.show()
            self.status_bar.showMessage("Ready")
            return
        if os.path.exists(temp_file):
            os.unlink(temp_file)
        self.update_preview()
        self.show()
        self.activateWindow()
        self.status_bar.showMessage("Ready")
        self.tool_combo.setCurrentText("Rectangle")
        self.current_tool = "rectangle"

    def update_preview(self):
        if self.pixmap:
            scaled_pixmap = self.pixmap.scaled(self.preview_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.preview_label.setPixmap(scaled_pixmap)
            self.preview_label.setStyleSheet("""
                background-color: #2E2E2E;
                border-radius: 5px;
            """)
        else:
            self.preview_label.clear()
            self.preview_label.setText("")
            self.preview_label.setStyleSheet("background-color: transparent;")

    def upload_image(self):
        if not (self.use_imgur and self.imgur_client_id) and not (self.use_gyazo and self.gyazo_api_key):
            self.show_message("Error", "Please set and enable at least one API (Imgur or Gyazo).", QMessageBox.Warning)
            self.set_api_keys()
            return
        if not self.pixmap:
            self.show_message("Error", "No screenshot to upload.", QMessageBox.Warning)
            if self.notification:
                self.notification.update_message("No screenshot to upload")
            else:
                self.notification = NotificationWidget("No screenshot to upload", parent=self)
                self.notification.show()
            return
        self.status_bar.showMessage("Uploading...")
        self.hide()
        self.notification = NotificationWidget("Uploading...", parent=self)
        self.notification.show()
        temp_file = os.path.join(tempfile.gettempdir(), f"graybyte_screenshot_{uuid.uuid4().hex}.png")
        self.pixmap.save(temp_file, "PNG")
        file_size = os.path.getsize(temp_file) / 1024
        start_time = time.time()
        url = None
        try:
            if self.use_imgur and self.imgur_client_id:
                url = self.upload_to_imgur(temp_file, file_size, start_time)
            if not url and self.use_gyazo and self.gyazo_api_key:
                url = self.upload_to_gyazo(temp_file, file_size, start_time)
            if not url:
                raise Exception("Upload failed: No valid API response")
            self.clear_canvas()
        except Exception as e:
            self.notification.update_message(f"Upload failed: {str(e)}")
            self.show_message("Error", f"Upload failed: {str(e)}", QMessageBox.Critical)
            self.clear_canvas()
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
            self.status_bar.showMessage("Ready")
            self.tool_combo.setCurrentText("Rectangle")
            self.current_tool = "rectangle"

    def upload_to_imgur(self, file_path, file_size, start_time):
        try:
            with open(file_path, "rb") as f:
                headers = {"Authorization": f"Client-ID {self.imgur_client_id}"}
                files = {"image": f}
                session = requests.Session()
                retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
                session.mount('https://', HTTPAdapter(max_retries=retries))
                response = session.post("https://api.imgur.com/3/image", headers=headers, files=files, timeout=30)
                if response.status_code == 401:
                    raise Exception("Imgur: Invalid Client-ID")
                response.raise_for_status()
                result = response.json()
                url = result.get("data", {}).get("link")
                if url:
                    elapsed_time = time.time() - start_time
                    upload_speed = file_size / elapsed_time if elapsed_time > 0 else 0
                    try:
                        QApplication.clipboard().setText(url)
                    except Exception as e:
                        try:
                            subprocess.run(["xclip", "-selection", "clipboard"], input=url.encode(), check=True)
                        except (FileNotFoundError, subprocess.CalledProcessError) as e:
                            self.show_message("Warning", f"Failed to copy URL to clipboard: {url}", QMessageBox.Warning)
                    self.status_bar.showMessage(f"Uploaded, Speed: {upload_speed:.2f} KB/s")
                    self.notification.update_message(f"- GRAYBYTE - SHOT n UP -\n{url}\nSpeed: {upload_speed:.2f} KB/s", url=url)
                    return url
                raise Exception("Imgur: No URL returned")
        except Exception as e:
            return None

    def upload_to_gyazo(self, file_path, file_size, start_time):
        try:
            with open(file_path, "rb") as f:
                files = {
                    "imagedata": ("screenshot.png", f, "image/png"),
                    "access_token": (None, self.gyazo_api_key)
                }
                session = requests.Session()
                retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
                session.mount('https://', HTTPAdapter(max_retries=retries))
                response = session.post("https://upload.gyazo.com/api/upload", files=files, timeout=30)
                if response.status_code == 401:
                    raise Exception("Gyazo: Invalid API key")
                response.raise_for_status()
                result = response.json()
                url = result.get("permalink_url")
                if url:
                    elapsed_time = time.time() - start_time
                    upload_speed = file_size / elapsed_time if elapsed_time > 0 else 0
                    try:
                        QApplication.clipboard().setText(url)
                    except Exception as e:
                        try:
                            subprocess.run(["xclip", "-selection", "clipboard"], input=url.encode(), check=True)
                        except (FileNotFoundError, subprocess.CalledProcessError) as e:
                            self.show_message("Warning", f"Failed to copy URL to clipboard: {url}", QMessageBox.Warning)
                    self.status_bar.showMessage(f"Uploaded, Speed: {upload_speed:.2f} KB/s")
                    self.notification.update_message(f"- GRAYBYTE - SHOT n UP -\n{url}\nSpeed: {upload_speed:.2f} KB/s", url=url)
                    return url
                raise Exception("Gyazo: No URL returned")
        except Exception as e:
            return None

    def save_locally(self):
        if not self.pixmap:
            self.show_message("Error", "No screenshot to save.", QMessageBox.Warning)
            return
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False, dir=tempfile.gettempdir()) as tmp:
            self.pixmap.save(tmp.name, "PNG")
            subprocess.run(["xdg-open", tmp.name])
            self.status_bar.showMessage("Saved locally")

    def clear_canvas(self):
        self.shapes = []
        self.pixmap = None
        self.preview_label.clear()
        self.update_preview()
        self.status_bar.showMessage("Canvas cleared")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraybyteImageUploader()
    sys.exit(app.exec_())
