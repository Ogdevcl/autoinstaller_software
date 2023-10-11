@echo off
echo Installiere PyQt5...
python -m pip install PyQt5

if errorlevel 1 (
    echo Fehler beim Installieren von PyQt5.
    pause
) else (
    echo PyQt5 wurde erfolgreich installiert.
    pause
)
