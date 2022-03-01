@echo on
pyinstaller --onefile "main.py" --name "JLWE10_OF_Team_Editor_v3" --noconsole --version-file file_version_info.txt
pause