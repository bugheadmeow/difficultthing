# TODO Найдите количество книг, которое можно разместить на дискете
amount = 1.44
number = 100
number_str = 50
number_letters = 25
one_letter = 4
amount_one = amount * 1024 * 1024
page = number * number_str * number_letters
page_count = page * one_letter
books = amount_one // page_count
print("Количество книг, помещающихся на дискету:", int(books))
