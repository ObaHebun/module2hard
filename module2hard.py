import random
field1 = random.randint(3, 21)
print(field1)
result = ""
for field1_1 in range(1, 21):
    for field1_2 in range(field1_1 + 1, 21):
        if field1 % (field1_1 + field1_2) == 0:
            result += str(field1_1) + str(field1_2)
print(result)
