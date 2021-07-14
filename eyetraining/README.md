## ==	Описание	==
Простейший тренажер для глаз.  
Нужно совмещать с легким морганием.  
  
Окно заполняет весь экран, на нем перемещается шарик.  
Есть несколько режимов перемещения шарика:  
1. Хаотичное перемещение шарика (текст внутри)  
2. Перемещение по различным круговым траекториям
Есть возможность поменять направление вращения и скорость  
перемещения шарика
## ==	Что потребуется	==
Потребуется python3, а также библиотека tkinter, она обычно в комплекте с питоном

## ==	Использование	== 
Запустить **python3 eye.py** или просто **make**

Кнопками + и - можно менять скорость перемещения шарика,  
в диапазоне от 0.2 до 5 секунд, с шагом 0.1 с  
По умолчанию - 1 с  
Кнопками с 1 по 6 меняется режим перемещения шарика.  
Кнопкой r меняется направление вращения.  
Вращение по умолчанию - по часовой стрелке.  

## == Hotkeys ==
1 - режим хаотичного перемещения  
В это режиме шарик появляется в различных местах экрана,  
при этом внутри шарика каждое перемещение обновляется буква из большой цитаты  
(весьма мудрой)  
2 - 6 - режимы вращения окружности/части окружности  
2 - вращение по полному кругу  
3 - вращение по нижнему полукругу  
4 - вращение по верхнему полукругу  
5 - вращение по спирали  
6 - вращение по знаку ∞  
r - смена направления вращения  
'+' - увеличение скорости вращения/перемещения  
'-' - уменьшение скорости вращения  
esc - выход из программы

## ==	Создано с помощью	==
python3