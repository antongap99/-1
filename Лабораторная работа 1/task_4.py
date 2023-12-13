def generate_visit_statistics(users_visits):
    statistics = {"Общее количество": 0, "Уникальные посещения": 0}

    statistics["Общее количество"] = len(users_visits)

    unique_visits = set(users_visits)
    statistics["Уникальные посещения"] = len(unique_visits)

    return statistics

users_visits = ["user1", "user2", "user1", "user3", "user2", "user4"]
statistics_result = generate_visit_statistics(users_visits)
print(statistics_result)