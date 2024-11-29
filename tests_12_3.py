'''
Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2.
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
Пример результата выполнения тестов:
Вывод на консоль:
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
----------------------------------------------------------------------
Ran 6 tests in 0.000s OK (skipped=3)

Файлы suite_12_3.py и tests_12_3.py, где произошли изменения загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''

import unittest
from unittest import TestCase
import random
import runner_and_tournament as rat
import runner

class RunnerTest(unittest.TestCase):
    @unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1=runner.Runner('бегун 1')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = runner.Runner('бегун 2')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1=runner.Runner('бегун 1')
        runner2=runner.Runner('бегун 2')

        runner1.walk()
        runner2.run()

        self.assertNotEqual(runner1.distance,runner2.distance)


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
                print(i)

    @unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test1_start(self):
        tir1 = rat.Tournament(90, self.runner1, self.runner3)
        res=tir1.start()
        results={}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[0] = results

    @unittest.skipIf(random.choice([True,False]),'Не повезло,Тесты в этом кейсе заморожены')
    def test2_start(self):
        tir2 = rat.Tournament(90, self.runner2, self.runner3)
        res=tir2.start()
        results = {}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[1] = results

    @unittest.skipIf(random.choice([True, False]), 'Не повезло,Тесты в этом кейсе заморожены')
    def test3_start(self):
        tir3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        res=tir3.start()
        results = {}
        for key,value in res.items():
            results[key]=value.name
        self.all_results[2]=results