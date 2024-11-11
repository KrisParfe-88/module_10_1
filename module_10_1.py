from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = datetime.now()
diff = finish - start
print(f'Работа потоков {diff}')
start = datetime.now()
threads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

for i in threads:
    i.start()

for i in threads:
    i.join()

finish = datetime.now()
diff = finish - start
print(f'Работа потоков {diff}')
