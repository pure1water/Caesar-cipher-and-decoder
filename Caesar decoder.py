#дешифратор

alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
k = int(input('Введите число сдвига: '))
msg = input('Введите сообщение, которое надо дешифровать: ')
result = ''

if k > 33:
    k = k%33

for i in msg:
    mesto = alph.find(i)
    n_mesto = (mesto - k)%33
    if i in alph:
        result += alph[n_mesto]

print(result)