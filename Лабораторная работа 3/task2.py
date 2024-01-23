def find_common_participants(group1, group2, delimiter=','):

    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    # Находим общих участников
    common_participants = set(participants1) & set(participants2)
    print(common_participants)

    return sorted(list(common_participants))


# test case
group1 = "Иванов,Петров,Сидоров,Смирнов"
group2 = "Петров,Смирнов,Козлов,Кузнецов"

print(find_common_participants(group1, group2))