def divide_players(players):
    total_players = len(players)

    middle_index = total_players // 2
    team1 = players[:middle_index]
    team2 = players[middle_index:]

    # Вывод результатов
    print("Команда 1:", team1)
    print("Команда 2:", team2)

# Пример использования функции
players_list = ["Игрок1", "Игрок2", "Игрок3", "Игрок4", "Игрок5", "Игрок6", "Игрок7", "Игрок8"]
players_list1 = ["Игрок1", "Игрок2", "Игрок3", "Игрок4", "Игрок5", "Игрок6", "Игрок7", "Игрок8", "Игрок9"]
divide_players(players_list)
divide_players(players_list1)