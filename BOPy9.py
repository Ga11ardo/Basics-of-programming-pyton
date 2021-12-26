def type_number(str):
    arr = []
    for i in range(0,len(str)):
        if str[i].isdigit():
            arr.append(int(str[i]))
    return arr

def print_digits(arr):
    print("Найдено "+str(len(arr))+" цифр(-а):", end =' ')
    for i in arr:
        print(str(i), end =' ')
    print('')

def receive_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

sequence = input("Введите последовательность цифровых символов: ")
num = type_number(sequence) 
print_digits(num)
sum = receive_sum(num)
print("Сумма цифр: " + str(sum))