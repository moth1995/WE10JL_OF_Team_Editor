@echo on
pyinstaller --onefile "main.py" --name "JLWE10_OF_Team_Editor" --noconsole --version-file file_version_info.txt
pause