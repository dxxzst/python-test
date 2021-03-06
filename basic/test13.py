import json
import unittest
from test12 import save_and_read, ForUnitTest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")  # 会分别在每调用一个测试方法的前被执行。

    def tearDown(self) -> None:
        print("tearDown")  # 会分别在每调用一个测试方法的后被执行。

    def test_save_and_read(self):
        file_name = "numbers.json"
        data1 = save_and_read(file_name)
        with open(file_name, mode='r') as f:
            data2 = json.load(f)
        self.assertEqual(data1, data2)

    def test_for_unit_test(self):
        for_test = ForUnitTest("Hi?")
        for_test.add_response("Yes!")
        self.assertIn("Yes!", for_test.response)


if __name__ == '__main__':
    unittest.main()
