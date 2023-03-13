number_of_tickets = int(input("Введите количество билетов: "))
amount = 0
for i in range(number_of_tickets):
    age = int(input(f'Введите возраст посетителя {i + 1}: '))
    if 18 <= age < 25:
        amount += 990
    elif age >= 25:
        amount += 1390
if number_of_tickets > 3:
    amount *= 0.9
print(f"Сумма к оплате: {amount} руб.")
