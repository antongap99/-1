import json

def calculate_product_sum_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Загрузка данных из JSON файла
            data = json.load(file)

            # Вычисление произведений и нахождение суммы
            product_sum = sum(entry["score"] * entry["weight"] for entry in data)

            # Округление до 3 знаков после запятой
            rounded_sum = round(product_sum, 3)

            return rounded_sum

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON: {e}")
        return None


result = calculate_product_sum_from_file('./data.json')
print(f"Сумма произведений: {result}")