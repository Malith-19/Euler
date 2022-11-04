total = 0
with open("inputs/problem13.txt") as file:
    for number in file:
        number = int(number.strip())
        total += number

print(str(total)[:10])