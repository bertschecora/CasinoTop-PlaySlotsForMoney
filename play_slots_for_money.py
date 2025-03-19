import random

print("Играть в игровые автоматы на деньги - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Играй на деньги в топ-казино и срывай куш!")
