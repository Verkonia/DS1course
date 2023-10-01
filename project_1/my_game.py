import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = 50 # поскольку угадываем значения от 1 до 100, изначально для сравнение берем значение 50
    count = 1 # поскольку за начальное значение берем число 50, считаем, что 1 попытка угадывания уже есть
    
    while predict_number != number:
        while  predict_number > number:
            predict_number -= 10
            count += 1
            while predict_number < number:
                predict_number += 1
                count += 1
        while  predict_number < number:
            predict_number += 10
            count += 1
            while predict_number > number:
                predict_number -= 1
                count += 1
    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)