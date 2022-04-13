from dataclasses import asdict, dataclass
from typing import Dict, List, Type

SWIMMING_WORKOUT: str = 'SWM'
RUNNING_WORKOUT: str = 'RUN'
SPOTSWALKING_WORKOUT: str = 'WLK'


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке.
    тип тренировки, длительность, дистанция,
    средняя скорость, потрачено килокалорий"""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (
            'Тип тренировки: {training_type}; '
            'Длительность: {duration:.3f} ч.; '
            'Дистанция: {distance:.3f} км; '
            'Ср. скорость: {speed:.3f} км/ч; '
            'Потрачено ккал: {calories:.3f}.'
        ).format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weihgt = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Метод не определен')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    COEFFICIENT_CALORIES_1: int = 18
    COEFFICIENT_CALORIES_2: int = 20

    def get_spent_calories(self) -> float:

        return ((self.COEFFICIENT_CALORIES_1 * self.get_mean_speed()
                - self.COEFFICIENT_CALORIES_2)
                * self.weihgt / self.M_IN_KM
                * self.duration * self.MIN_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    WALKING_COEFFICIENT_1: float = 0.035
    WALKING_COEFFICIENT_2: float = 0.029

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.WALKING_COEFFICIENT_1 * self.weihgt
                 + (self.get_mean_speed() ** 2 // self.height)
                 * self.WALKING_COEFFICIENT_1 * self.weihgt)
                * self.duration * self.MIN_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    SWIM_COEF_1: float = 1.1
    SWIM_COEF_2: int = 2

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.SWIM_COEF_1)
                * self.SWIM_COEF_2 * self.weihgt)


def read_package(workout_type: str, data: List[int]) -> Type[Training]:
    """Прочитать данные полученные от датчиков."""

    workout_types: Dict = {str, Type[Training]}
    workout_types = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    if workout_type in workout_types:
        return workout_types[workout_type](*data)
    raise ValueError('Тип тренировки не определен')


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        (SWIMMING_WORKOUT, [720, 1, 80, 25, 40]),
        (RUNNING_WORKOUT, [15000, 1, 75]),
        (SPOTSWALKING_WORKOUT, [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
