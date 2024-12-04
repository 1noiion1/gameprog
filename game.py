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

    def upp_lvl(self):
        """
        Метод, который увеличивает сложность игры, в зависимости от количества жизней игрока,
        посредством добавления локаций
        """
        if person.lives > 5:
            self.rooms.append('комнату с ловушками')
            self.rooms.append('комнату с монстром')


class Trap:
    """
    Класс, который представляет собой комнату с ловушками
    """
    def damage(self):
        """
        Метод, который возвращает количество оставшихся жизней после получения урона от ловушки
        :return: количество оставшихся жизней игрока
        """
        person.lives -= 1
        return f'У вас осталось {person.lives} жизней'


class Treasure:
    """
    Класс, который представляет собой комнату с сокровищами
    """
    def __init__(self):
        self.treasure = random.randint(1, 5) # получение от 1 до 5 очков

    def get_treasure(self):
        """
        Метод, который увеличивает количество очков игрока и возвращает информацию о текущем количестве очков
        :return: количество очков
        """
        person.bonus += self.treasure
        return f'Теперь у вас {person.bonus} очков'


class Monster:
    '''
    Класс, который представляет собой комнату с монстрами
    '''
    def __init__(self):
        self.monsters = ['Орк', 'Гоблин'] # Виды монстров
        self.ork = ['Победа!', 'Поражение!', 'Поражение!'] # Шанс победы над Орком
        self.goblin = ['Победа!', 'Поражение!'] # Шанс победы над Гоблином

    def random_monster(self):
        """
        Метод, который возвращает рандомного монстра
        :return: рандомный монстр
        """
        return ''.join(random.choices(self.monsters))

    def random_win(self):
        """
        Метод, который представляет бой с монстром
        :return: победа или проигрыш игрока
        """
        if random_monster == 'Орк':
            rand_ork = random.choice(self.ork)
            if rand_ork == 'Победа!':
                person.bonus += 5
                return f'Поздравляю! Вы победили! Теперь у вас {person.bonus} очков'
            else:
                person.lives -= 2
                return f'Монстр одолел вас. У вас осталось {person.lives} жизней'

        elif random_monster == 'Гоблин':
            rand_goblin = random.choice(self.goblin)
            if rand_goblin == 'Победа!':
                person.bonus += 3
                return f'Поздравляю! Вы победили! Теперь у вас {person.bonus} очков'
            else:
                person.lives -= 1
                return f'Монстр одолел вас. У вас осталось {person.lives} жизней'

    def evade(self):
        """
        Метод, который представляет собой побег от монстра
        :return: количество потерянных жизней
        """
        lose_lives = random.randint(0, 1)
        person.lives -= lose_lives
        return f'Убегая, вы потеряли {lose_lives} жизней'


class Arsenal:
    """
    Класс, который представляет собой оружие
    """
    def __init__(self):
        self.arsenal = ['Меч', None, None, 'Нож', None, None, 'Дубинка', None, None]
        self.monsters_list = Monster()

    def arsenal_in_room(self):
        """
        Метод, который выдает рандомное оружие
        :return: рандомное оружие
        """
        try:
            arsenals = ''.join(random.choices(self.arsenal))
        except TypeError:
            return None

        if arsenals == 'Меч':
            self.monsters_list.ork.append('Победа!')
            self.monsters_list.goblin.append('Победа!')
            print(f'Вы нашли {arsenals}, теперь у вас есть оружие')

        elif arsenals == 'Нож':
            self.monsters_list.goblin.append('Победа!')
            print(f'Вы нашли {arsenals}, теперь у вас есть оружие')

        elif arsenals == 'Нож':
            self.monsters_list.ork.append('Победа!')
            print(f'Вы нашли {arsenals}, теперь у вас есть оружие')



print('Приветствую тебя в игре Сокровища и подземелья')
print('В начале игры тебе дается 3 жизни и 0 очков')
print('Передвигайся по комнатам и зарабатывай очки')


room = Room()
monster = Monster()
person = Person()
trap = Trap()
treasure = Treasure()
arsenal = Arsenal()


while person.lives > 0:
    room.upp_lvl()
    print('Введите направление:')
    answer_room = room.choice_direction(input())
    print(f'Вы попали в {answer_room}')
    if answer_room == 'комнату с ловушками':
        print(trap.damage())
    elif answer_room == 'сокровищницу':
        print(treasure.get_treasure())
        arsenal.arsenal_in_room()
        person.reverse()
    elif answer_room == 'комнату с монстром':
        random_monster = monster.random_monster()
        print(f'В комнате находится {random_monster}. Будете сражаться? (Нет/Да)')
        answer_monster = input().lower()
        if answer_monster == 'да':
            print(monster.random_win())
            person.reverse()
        else:
            print(monster.evade())
            print(f'У вас осталось {person.lives} жизней')

    elif answer_room == 'выход!':
        print('Вы хотите покинуть подземелье? Да/Нет')
        answer_exit = input().lower()
        if answer_exit == 'нет':
            continue
        else:
            print(f'Вы выбрались. Ваши очки: {person.bonus}')
            break


else:
    print('У вас не осталось жизней. Вы проиграли')
