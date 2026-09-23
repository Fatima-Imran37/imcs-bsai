numbers = [ ]
even_count = 0
odd_count = 0

for i in range(1, 11):
    n = int(input(f"Enter number {i}: "))
    numbers.append(n)
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

total = sum(numbers)
average = total / 10

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")