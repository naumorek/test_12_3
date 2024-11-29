import unittest
from unittest import TestCase
import tests_12_3 as t1

ratST=unittest.TestSuite()
ratST.addTest(unittest.TestLoader().loadTestsFromTestCase((t1.TournamentTest)))
ratST.addTest(unittest.TestLoader().loadTestsFromTestCase((t1.RunnerTest)))
runner=unittest.TextTestRunner(verbosity=2)
runner.run(ratST)