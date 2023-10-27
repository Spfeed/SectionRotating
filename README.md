# Вращение отрезка с заданными точками начала и конца вокруг точки с заданной угловой скоростью
[![Build, Test](https://github.com/Spfeed/SectionRotating/actions/workflows/ci.yml/badge.svg)](https://github.com/Spfeed/SectionRotating/actions/workflows/ci.yml)
[![License: MIT ](https://img.shields.io/badge/License-MIT-fuchsia.svg)](https://opensource.org/licenses/MIT)

## Иллюстрация работы приложения

![](https://github.com/Spfeed/SectionRotating/blob/master/utils/section.gif)

## Предварительные условия

- Python 3.11;
- Библиотека Tkinter;
- Библиотека Unittest.

## Установка

1. Клонируйте репозиторий или скопируйте исходный код;
    ```
    git clone https://github.com/Spfeed/SectionRotating.git
    ```
2. Скачайте [Python](https://www.python.org/);
3. Перейдите в директорию проекта, введя команду:
    ```
    cd SectionRotating
    ```
4. Установите необходимые библиотеки, введя команду:
    ```
    pip install -r libraries.txt
    ```

## Использование

1. Откройте терминал и перейдите в директорию, в которой находится программа;
2. Введите и выполните следующую команду:
   ```
     python src/main.py
     ```
3. Введите координаты точек начала и конца отрезка в поля x_start, y_start, x_end, y_end;
4. Введите координаты точки вращения x_rotate, y_rotate и значение угловой скорости angular_speed;
5. Нажмите на клавишу кнопку "Ввод";
6. На экране отобразится отрезок, вращающийся вокруг точки с заданными координатами и угловой скоростью;
7. После завершения работы можно нажать клавишу Esc для закрытия приложения.

## Функции 

- Ввод значений точек координат и угловой скорости;
- Отрисовка отрезка;
- Вращение отрезка вокруг заданной точки;
- Выход из приложения по нажатию на клавишу Esc.

  ## Создано с помощью

- [Python](https://www.python.org/);
- [Tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter).
