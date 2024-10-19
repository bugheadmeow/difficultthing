from os import remove

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers.remove(None)

average = round(sum(numbers) / (len(numbers) + 1), 2)
numbers.insert(4, average)

print("Измененный список:", numbers)
