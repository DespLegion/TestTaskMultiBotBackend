import random


class TestingGen:
    def __init__(self, test_count: int = 5):
        self.test_count = test_count

    def generate(self):
        testings = []

        for i in range(0, self.test_count):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            r_answer = a + b
            f_answer_1 = random.randint(1, 300)
            f_answer_2 = random.randint(1, 300)
            f_answer_3 = random.randint(1, 300)

            answers = {
                "r_answer": r_answer,
                "f_answer_1": f_answer_1,
                "f_answer_2": f_answer_2,
                "f_answer_3": f_answer_3
            }
            answers_keys = list(answers.keys())
            random.shuffle(answers_keys)

            shuf_answers = {}
            for key in answers_keys:
                shuf_answers[key] = answers[key]

            testings.append(
                {
                    "question": f"{a} + {b} = ?",
                    "answers": shuf_answers,
                }
            )
        return testings
