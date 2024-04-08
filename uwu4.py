def calculate_average(numbers):
    total = 0
    count = 0
    average = 0
    for num in numbers:
        total += num
        count += 1
        average = total / count
    return average


nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = calculate_average(nums)
print(result)