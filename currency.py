
limit = int(input("Enter the number of coins: "))
coins = []
for i in range(limit):
    coins.append(int(input(f"Enter the value of coin{i+1}: ")))

coins.sort()
print(f"Coins you entered is: {coins}")
note = int(input("Enter the value of currency note: "))
count = limit - 1
flag = 0
print()
for i in range(limit - 1, -1, -1):
    if note % coins[i] == 0:
        flag = int(note / coins[i])
        print(f"{coins[i]} * {flag} coins")
        break

if flag == 0:
    while note != 0:
        denominator = coins[count]
        value = note / denominator
        if value >= 1:
            print(f"{denominator} * {int(value)} coins")
        note = note % denominator
        flag = flag + int(value)
        count = count - 1
        if count < 0 and note is not 0:
            print(f"The remaining Currency value: {note}")
            break

print(f"\nNumber of minimum coin needed: {flag}")



# while note != 0:
#     denominator = coins[count]
#     value = note / denominator
#     if value >= 1:
#         print(f"{denominator} * {int(value)} coins")
#     note = note % denominator
#     flag = flag + int(value)
#     count = count - 1
#     if count < 0 and note is not 0:
#         print(f"The remaining Currency value: {note}")
#         break
#
# print(f"\nNumber of minimum coin needed: {flag}")
