import json
from random import randint


def save_and_read(filename):
    numbers = [randint(0, 13) for i in range(0, 10)]
    print(numbers)

    # filename = 'numbers.json'
    with open(filename, mode='w') as f:
        json.dump(numbers, f)

    with open(filename, mode='r') as f:
        data = json.load(f)
        print(data)
    return data


class ForUnitTest:
    """测试unit test"""

    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def add_response(self, res):
        self.response.append(res)

    def show_results(self):
        print("show all results:")
        for item in self.response:
            print(f"-{item}")


if __name__ == '__main__':
    save_and_read('numbers.json')
