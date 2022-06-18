@echo on
set PY_FILE=of_team_editor.py
set PROJECT_NAME=PES WE J League OF Team Editor 2006-2010
set VERSION=1.0
set FILE_VERSION=file_version_info.txt
set EXTRA_ARG=--add-data=resources/img/*;resources/img --add-data=resources/demonyms.csv;resources 

pyinstaller --onefile "%PY_FILE%" --name "%PROJECT_NAME%_%VERSION%" --noconsole %EXTRA_ARG% --version-file "%FILE_VERSION%"

Rem This command below is just specific for this script

Xcopy /E ".\config\" ".\dist\config\"

Rem end of extra command

cd dist
tar -acf "%PROJECT_NAME%_%VERSION%_release.zip" *
pause
