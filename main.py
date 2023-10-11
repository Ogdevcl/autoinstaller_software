import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QMessageBox
import subprocess
import os

class InstallationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anwendungsinstallation")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Titellabel
        title_label = QLabel("<h2>Willkommen zur Anwendungsinstallation</h2>")
        layout.addWidget(title_label)

        # Anwendungscheckboxes
        checkboxes_layout = QVBoxLayout()
        self.avira_checkbox = QCheckBox("Avira 64_BIT")
        self.office_checkbox = QCheckBox("Apache Office 64_BIT")
        self.firefox_checkbox = QCheckBox("Firefox 64_BIT")
        checkboxes_layout.addWidget(self.avira_checkbox)
        checkboxes_layout.addWidget(self.office_checkbox)
        checkboxes_layout.addWidget(self.firefox_checkbox)
        layout.addLayout(checkboxes_layout)

        # Installieren-Button
        install_button = QPushButton("Installieren")
        install_button.clicked.connect(self.install_applications)
        layout.addWidget(install_button)

        # Support-Link
        support_label = QLabel('<a href="https://discord.gg/NzPSM9ycwr">Haben Sie Fragen? Besuchen Sie unseren Discord-Server</a>')
        support_label.setOpenExternalLinks(True)
        layout.addWidget(support_label)

        # Entwickler-Label
        developer_label = QLabel('<a href="GitHub Link">Made by Ravi</a>')
        developer_label.setOpenExternalLinks(True)
        layout.addWidget(developer_label)

    def install_applications(self):
        selected_apps = []
        if self.avira_checkbox.isChecked():
            selected_apps.append("Avira")
        if self.office_checkbox.isChecked():
            selected_apps.append("Apache Office")
        if self.firefox_checkbox.isChecked():
            selected_apps.append("Firefox")

        if not selected_apps:
            QMessageBox.warning(self, "Warnung", "Bitte wählen Sie mindestens eine Anwendung zum Installieren aus.")
            return

        for app in selected_apps:
            try:
                if app == "Avira":
                    subprocess.run(r'avira_de.exe', shell=True)
                elif app == "Apache Office":
                    subprocess.run(r'Apache_OpenOffice.exe', shell=True)
                elif app == "Firefox":
                    subprocess.run(r'Firefox Installer.exe', shell=True)
                QMessageBox.information(self, "Installation abgeschlossen", f"Die Installation von {app} wurde erfolgreich abgeschlossen.")
            except subprocess.CalledProcessError as e:
                if e.returncode == 740:
                    # Fehlercode 740 bedeutet, dass die Installation als Administrator verweigert wurde
                    result = QMessageBox.question(self, "Fehler", f"Die Installation von {app} als Administrator wurde verweigert. Möchten Sie erneut versuchen?",
                                                  QMessageBox.Yes | QMessageBox.No)
                    if result == QMessageBox.Yes:
                        self.install_applications()
                    else:
                        QMessageBox.information(self, "Installation abgebrochen", f"Die Installation von {app} wurde abgebrochen.")
                else:
                    QMessageBox.critical(self, "Fehler", f"Es ist ein Fehler aufgetreten: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstallationGUI()
    window.show()
    sys.exit(app.exec_())
