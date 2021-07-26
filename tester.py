import timeit
from subprocess import Popen, PIPE


def get_input(path):
    with open(path, "rb") as f:
        return f.read()


def get_answer(path):
    with open(path, "rb") as f:
        return f.readlines()


SC = 1  # successfully completed
WA = 2  # wrong answer
RE = 3  # runtime error
TL = 4  # time limit


def different_length_message(correct, user):
    return f"Different length\n" \
           f"Correct: {correct}\n" \
           f"Your: {user}"


def different_lines_message(correct, user, index):
    return f'Difference in lines {index}\n' \
           f'Correct: "{correct}"\n' \
           f'Your: "{user}"'


class ScriptTester:
    def __init__(self, cmd, time_limit=1, memory_limit=512, details=True):
        self.cmd = cmd
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.details = details

    def execute(self, stdin):
        with Popen(self.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            proc.stdin.write(stdin)
            proc.stdin.close()
            return proc.stdout.readlines(), proc.stderr.read().decode()

    def test(self, input_path, answer_path) -> (int, float, str):  # verdict, execute_time, details
        start = timeit.default_timer()
        stdout, stderr = self.execute(get_input(input_path))
        execute_time = timeit.default_timer() - start

        # runtime error
        if stderr:
            return RE, execute_time, stderr

        answer = get_answer(answer_path)

        #  different length
        answer_length = len(answer)
        stdout_length = len(stdout)
        if stdout_length != stdout_length:
            return WA, execute_time, different_length_message(answer_length, stdout_length)

        for index, variants in enumerate(zip(stdout, answer)):
            user, correct = map(bytes.strip, variants)
            if user != correct:
                return WA, execute_time, different_lines_message(correct, user, index)
