
total = 0
count = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to stop): "))

if count > 0:
    average = total / count

    print("Items:", count, "Total: {:.2f}".format(total))
    print("Average: {:.2f}".format(average))
else:
    print("Items: 0 Total: 0.00")
    print("Average: 0.00")
