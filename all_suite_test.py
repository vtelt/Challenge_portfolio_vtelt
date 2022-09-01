import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginPage
from test_cases.add_player_on_dashboard import TestDashboardPage
from test_cases.framework import Test

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestDashboardPage))

   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())