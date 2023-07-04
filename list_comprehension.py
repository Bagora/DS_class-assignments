def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Here are all the even numbers using list comprehension method {get_even_numbers(numbers)}")
