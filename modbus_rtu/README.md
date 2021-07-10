![Alt-текст](https://github.com/z34hyr/python_projects/blob/main/modbus_rtu/UI.png "User interface")

## ==	Описание	==
Скрипт позволяет определить адрес слейв-устройства в сети modbus-rtu(rs485),  
в случае, если устройство в сети, но мы не знаем его номер.

Сделан простенький пользовательский интрефейс на tkinter.

В первую очередь скрипт использован на использование под windows -  
не требуется установки никаких дополнительных компонентов,  
предоставляется исполняемый файл.

## ==	Что потребуется	==
Если пользуетесь на windows - ничего, просто распакуйте архив,
exe внутри.  
На Linux - потребуется python3, а также библиотека minimalmodbus  
_pip install minimalmodbus_

## ==	Использование	==
Для запуска на windows - запустить modbusrtu.exe строго из распакованной папки  
Для запуска на Linux - запустить python3 modbusrtu.py

1) Выбрать скорость (по умолчанию - 19200  baud)
2) Выбрать порт, к которому подключен преобразователь USB<->RS-485
3) Нажать кнопку "Начать поиск"
Под кнопкой находится тестовое поле, в котором отображается
текущая информация.
В случае отклика устройства, появится сообщение с его номером.

Если в сети несколько устройств, будет отображаться лишь одно - с меньшим адресом.

## ==	Создано с	==
python3  
Компиляция в .exe выполнена с помощью pyinstaller