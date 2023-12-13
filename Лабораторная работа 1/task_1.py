def find_and_replace_missing(lst):
    missing_index = lst.index(None)

    sum_without_missing = sum(num for index, num in enumerate(lst) if index != missing_index)
    count_without_missing = len(lst) - 1

    average = sum_without_missing / count_without_missing
    lst[missing_index] = average

    return lst

numbers = [1,2,3, None, 5]

print(find_and_replace_missing(numbers))