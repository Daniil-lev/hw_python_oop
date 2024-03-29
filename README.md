# Модуль фитнес-трекера / Fitness tracker module
(hw_python_oop - спринт 2)

## Описание
Программный модуль фитнес-трекера, обрабатывает данные для трех видов тренировок: для бега, спортивной ходьбы и плавания.
Создан в рамках работы с объектно-ориентированным программированием на языке Python.

***Модуль:***

- принимает от блока датчиков информацию о прошедшей тренировке;
- определяет вид тренировки;
- рассчитывает результаты тренировки;
- выводит информационное сообщение о результатах тренировки.

***На выходе, информационное сообщение о:***

- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.

## Запуск проекта:
 Модуль реализован на python, файл программы - **homework.py**
 
## Пример работы:
Входные данные:
```python
packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
```
Результат:
```
Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 0.994 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 336.000.
Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 699.750.
Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 157.500.
```

---
## Структура программы:
### Базовый класс
```python
class Training
```
***Свойства класса***
* action - основное считываемое действие во время тренировке (шаг - бег, ходьба; гребок - плавание);
* duration - длительность тренировки;
* weight - вес спортсмена;
* M_IN_KM = 1000 - константа для перевода значений из метров в километры. Её значение — 1000.
* LEN_STEP - расстояние, которое спортсмен преодолевает за один шаг или гребок. Один шаг — это  `0.65` метра, один гребок
при плавании — `1.38` метра.

***Методы класса***

* get_distance() - метод возвращает значение дистанции преодоленной за тренировку
```
# базовая формула расчета
шаг * LEN_STEP / M_IN_KM
```
* get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
```
# базовая формула расчета
дистанция / длительность
```
* get_spent_calories() - метод возвращает число потраченных калорий
* show_training_info() - метод возвращает объект возвращает объект класса сообщения

### Классы наследники
Класс беговой тренировки
```python
class Running
```
***Свойства класса***
наследуются

***Методы класса***
переопределить метод:
* get_spent_calories() - метод возвращает число потраченных калорий

```
# формула расчета
(18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
```

### Класс спортивной ходьбы
```python
class SportsWalking
```
***Свойства класса***
Добавляемые свойства:
* height - рост

***Методы класса***
преопределить метод:
* get_spent_calories() - метод возвращает число потраченных калорий
```
# формула расчета
(0.035 * вес + (скорость ** 2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
```
### Класс тренировки в бассейне
```python
class Swimming
```
***Свойства класса***
Добавляемые свойства:
* length_pool - длина бассейна
* count_pool - количество проплытых бассейнов

***Методы класса***
пререопределить метод:
* get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
```
# формула расчета
длина_бассейна * count_pool / M_IN_KM / время_тренеровки
```
* get_spent_calories() - метод возвращает число потраченных колорий
```
# формула расчета
(скорость + 1.1) * 2 * вес
```
### Класс информационного сообщения
```python
class InfoMessage
```
***Свойства класса***
* training_type - тип тренировки
* duration - длительность тренировки
* distance -дистанция преодоленная за тренировку
* speed - средняя скорость движения во время движения
* calories - потраченные за время тренировки килокалории

***Методы класса***

* get_message() - метод выводит возвращает строку сообщения:
```python
# выводимое сообщение
# все значения типа float округляются до 3 знаков после запятой
'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}'.
```

## Функции модуля
```python
def read_package()
```
* Функция read_package() принимает на вход код тренировки и список её параметров.
* Функция должна определить тип тренировки и создать объект соответствующего класса,
передав ему на вход параметры, полученные во втором аргументе. Этот объект функция должна вернуть.

```python
def main(training)
```
Функция `main()` должна принимать на вход экземпляр класса `Training`.

- При выполнении функции `main()`для этого экземпляра должен быть вызван метод `show_training_info()`;
результатом выполнения метода должен быть объект класса `InfoMessage`, его нужно сохранить в переменную `info`.
- Для объекта `InfoMessage`, сохранённого в переменной `info`, должен быть вызван метод,
который вернет строку сообщения с данными о тренировке; эту строку нужно передать в функцию `print()`.
