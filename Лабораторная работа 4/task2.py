import csv
import json
def csv_to_json(csv_file_path, delimiter=',', newline='\n'):
    try:
        with open(csv_file_path, 'r', newline=newline, encoding='utf-8') as csvfile:
            # Используем DictReader для чтения CSV и преобразования в словари
            csv_reader = csv.DictReader(csvfile, delimiter=delimiter)

            # Создаем список для хранения словарей
            json_data = []

            # Проходим по каждой строке CSV файла
            for row in csv_reader:
                # Добавляем словарь в список
                json_data.append(dict(row))

            # Преобразуем список словарей в JSON с отступами
            json_string = json.dumps(json_data, indent=4, ensure_ascii=False)

            # Выводим JSON строку
            print(json_string)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

csv_to_json('./data.csv')