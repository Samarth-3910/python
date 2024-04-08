cats = ["Fluffy", "Whiskers"]
num_feedings_per_day = int(input())

for feeding_number in range(1, num_feedings_per_day + 1):
    for cat in cats:
        print(feeding_number, end=" ")
