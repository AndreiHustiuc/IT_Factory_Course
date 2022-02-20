import unittest
import HtmlTestRunner

from src.home_work.part_2_automation import oop_test_login


class TestSuite(unittest.TestCase):

    def test(self):
        log_in = unittest.TestSuite()
        log_in.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(oop_test_login.Login))

        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(log_in)


if __name__ == "__main__":
    unittest.main()