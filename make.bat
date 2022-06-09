@echo on
set PY_FILE=of_team_editor.py
set PROJECT_NAME=J League WE 10 OF Team Editor
set VERSION=3.0
set FILE_VERSION=file_version_info.txt
set EXTRA_ARG=--add-data=img;img

pyinstaller --onefile "%PY_FILE%" --name "%PROJECT_NAME%_%VERSION%" --noconsole %EXTRA_ARG% --version-file "%FILE_VERSION%"

Rem This command below is just specific for this script

rem Xcopy /E ".\config\" ".\dist\config\"

Rem end of extra command

cd dist
tar -acf "%PROJECT_NAME%_%VERSION%_release.zip" *
pause





rem @echo on
rem pyinstaller --onefile "main.py" --name "J League WE 10 OF Team Editor" --noconsole --add-data=img;img --version-file file_version_info.txt
rem pause
