import random


def random_numbers():
    numbers = set()

    while len(numbers) < 5:
        random_number = random.randint(0, 90)
        numbers.add(random_number)

    return numbers


winning_numbers = random_numbers()
my_numbers = random_numbers()

my_winning_numbers = winning_numbers.intersection(my_numbers)

print(f"My winning numbers: {my_winning_numbers} \n"
      f"# hit: {len(my_winning_numbers)}")
