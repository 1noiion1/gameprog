import random

class Person:
    """
    Класс, который представляет количество очков и количество жизней игрока
    """
    def __init__(self):
        self.lives = 3
        self.bonus = 0

    def reverse(self):
        """
        Метод, который преобразует очки в жизни и выводит информацию о текущем количестве жизней и очков
        """
        if 10 <= self.bonus < 20:
            self.lives += 1
            self.bonus -= 10
            print(f'Вы набрали достаточно очков для пополнения жизней. '
                  f'Теперь у вас {self.bonus} очков и {self.lives} жизней')


class Room:
    """
    Класс, который представляет комнаты/локации
    """
    def __init__(self):
        self.rooms = ['сокровищницу', 'комнату с ловушками', 'комнату с монстром', 'выход!']

    def choice_direction(self, choice):
        """
        Метод, который возвращает рандомную комнату
        :param choice: направление, выбранное игроком
        :return: рандомная комната
        """
        if choice == 'вперед' or choice == 'налево' or choice == 'направо' or choice == 'назад':
            return ''.join(random.choices(self.rooms))