def palidrome_check(string):
    prepared_string = string.replace(" ", "").lower()
    return prepared_string == prepared_string[::-1]

s = input("Введите слово: ")
answer = palidrome_check(s)
print(answer)
