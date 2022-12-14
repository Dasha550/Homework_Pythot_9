#5. Дана строка в виде случайной последовательности чисел от 0 до 9.

#Требуется создать словарь, который в качестве ключей будет 
# принимать данные числа (т. е. ключи будут типом int), 
# а в качестве значений – количество этих чисел в имеющейся последовательности. 
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
def count_it(sequence):
    numFrequence = {int(item): sequence.count(item) for item in sequence}
    sortNumFrequence = sorted(numFrequence.items(), key=lambda elem: elem[1])
    return dict(sortNumFrequence[-3:])
print(count_it('11111223333344555555'))