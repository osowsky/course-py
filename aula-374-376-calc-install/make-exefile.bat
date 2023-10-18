set PRJ_PATH=../aula-346-373-calc
set ARG_PROJ=%PRJ_PATH%/main.py
set ARG_GENL=--noconfirm --noconsole --onefile --clean --log-level=WARN
set ARG_PATH=--distpath=./dist --workpath=./build --specpath=./
set ARG_APPL=--name="Calculadora" --icon=%PRJ_PATH%/files/icon.png
set ARG_DATA=--add-data=%PRJ_PATH%/files/;./files/

pyinstaller %ARG_GENL% %ARG_APPL% %ARG_DATA% %ARG_PATH% %ARG_PROJ%
