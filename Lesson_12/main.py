numbers = {1:"one", 2: "two", 3:"three"}
print(numbers[1])
print(numbers[2])
print(numbers[3])

# breakpoint()

print ('-------------- ')
for y in range(1, 3+1):
    for x in range(1, 3+1):
        print(f"{y} {x}", end=" ")
    print()
    print ("-------------- ")

print("Выполнение завершено")
print("Все выведено")
print("Можно заканчивать отладку")



# python -m pdb main.py
