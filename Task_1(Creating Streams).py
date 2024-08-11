"""
Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
    1) 10, example1.txt
    2) 30, example2.txt
    3) 200, example3.txt
    4) 100, example4.txt

После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
    1) 10, example5.txt
    2) 30, example6.txt
    3) 200, example7.txt
    4) 100, example8.txt

Примечания:
1) Не переживайте, если программа выполняется долго, учитывая кол-во слов,
максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
2) Следует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt,
т.к. потоки работали почти одновременно.
"""
from threading import Thread
from time import sleep, time


def ite_words(word_count: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово №{word}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':
    # замеряем время начала выполнения программы с 1-м потоком
    start_time1 = time()

    # запускаем программу
    ite_words(10, 'example1.txt')
    ite_words(30, 'example2.txt')
    ite_words(200, 'example3.txt')
    ite_words(100, 'example4.txt')

    # замеряем время окончания выполнения программы с 1-м потоком
    end_time1 = time()
    execution_time1 = end_time1 - start_time1
    print(f"Время работы 1-го потока {execution_time1:.2f}")

    # замеряем время начала выполнения программы c 4-ми потоками
    start_time2 = time()
    # создаем и настраиваем 4 потока для функции ite_words
    thread1 = Thread(target=ite_words, args=(10, 'example5.txt'))
    thread2 = Thread(target=ite_words, args=(30, 'example6.txt'))
    thread3 = Thread(target=ite_words, args=(200, 'example7.txt'))
    thread4 = Thread(target=ite_words, args=(100, 'example8.txt'))

    # запускаем потоки
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # дожидаемся завершения работы потоков
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # замеряем время окончания выполнения программы
    end_time2 = time()
    execution_time2 = end_time2 - start_time2
    print(f"Время работы 4-х потоков {execution_time2:.2f}")
