s = input('Введите строку: ')
char = input('Введите символ: ')
print(
f'''Первое вхождение с индексом {s.find(char)}
Последнее вхождение с индексом {s.rfind(char)}'''
)