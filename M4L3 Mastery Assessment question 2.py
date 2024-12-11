from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

# choose four items from the possibilities
chosen = [str(choice(possibilities)) for _ in range(4)]

# print the four chosen items
print(f"Any ticket matching {''.join(chosen)} wins a prize!")
