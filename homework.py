class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self: str,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = format(duration, '.3f')
        self.distance = format(distance, '.3f')  # сколько пробежал в км
        self.speed = format(speed, '.3f')  # в км/ч
        self.calories = format(calories, '.3f')  # потраченый жирок)

    def get_message(self) -> str:
        f1 = f'Тип тренировки: {self.training_type}; '
        f2 = f'Длительность: {self.duration} ч.; '
        f3 = f'Дистанция: {self.distance} км; '
        f4 = f'Ср. скорость: {self.speed} км/ч; '
        f5 = f'Потрачено ккал: {self.calories}.'
        f6 = f1 + f2 + f3 + f4 + f5
        return f6


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,  # число шагов или гребков
                 duration: float,  # длительность тренировки
                 weight: float,  # вес спотсмена
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weihgt = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        self.distance = self.action * self.LEN_STEP / self.M_IN_KM
        return self.distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        self.speed = self.get_distance() / self.duration
        return self.speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        message = InfoMessage(type(self).__name__,
                              self.duration,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories())
        return message


class Running(Training):  # свойства не изменяются
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        KOEF_COL_1 = 18  # хз откуда но такой придуман
        KOEF_COL_2 = 20
        self.calories = ((KOEF_COL_1 * self.get_mean_speed() - KOEF_COL_2)
                         * self.weihgt / self.M_IN_KM
                         * self.duration * self.MIN_IN_HOUR)
        return self.calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        walking_coef_1 = 0.035
        speed_koef = self.get_mean_speed() ** 2
        walking_coef_2 = 0.029
        self.calories = ((walking_coef_1 * self.weihgt
                         + (speed_koef // self.height)
                         * walking_coef_2 * self.weihgt)
                         * self.duration * self.MIN_IN_HOUR)
        return self.calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool  # длинна бассейна в метрах
        self.count_pool = count_pool  # сколько бассейнов проплыли

    def get_distance(self) -> float:
        self.distance = self.action * self.LEN_STEP / self.M_IN_KM
        return self.distance

    def get_mean_speed(self) -> float:
        self.speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return self.speed

    def get_spent_calories(self) -> float:
        SWIM_COEF_1 = 1.1
        SWIM_COEF_2 = 2
        self.calories = ((self.get_mean_speed() + SWIM_COEF_1)
                         * SWIM_COEF_2 * self.weihgt)
        return self.calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    dict_1 = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    training = dict_1[workout_type](*data)
    return training


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
