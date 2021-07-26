import timeit
from subprocess import Popen, PIPE


SC = 1  # successfully completed
WA = 2  # wrong answer
RE = 3  # runtime error
TL = 4  # time limit


def different_length_message(correct, user):
    return f"Different length\n" \
           f"\tCorrect: {correct}\n" \
           f"\tYour: {user}"


def different_lines_message(correct, user, index):
    return f'Difference in lines {index}\n' \
           f'\tCorrect: "{correct}"\n' \
           f'\tYour: "{user}"'


def time_limit_message(limit_time):
    return f'Time limit: {limit_time}'


class ScriptTester:
    def __init__(self, cmd, time_limit=1):
        self.cmd = cmd
        self.time_limit = time_limit

    def execute(self, stdin) -> (str, str, float):
        with Popen(self.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            start = timeit.default_timer()
            stdout, stderr = proc.communicate(stdin)
            execute_time = timeit.default_timer() - start
        return stdout, stderr, execute_time

    def test(self, stdin: bytes, answer: bytes) -> (int, float, str):  # verdict, execute_time, details
        stdout, stderr, execute_time = self.execute(stdin)

        print(stdout)
        output = stdout.decode()
        errors = stderr.decode()

        # runtime error
        if errors:
            return RE, execute_time, errors

        answer = answer.decode().split('\n')
        user = output.split('\n')

        #  different length
        answer_length = len(answer)
        user_length = len(user)
        if answer_length != user_length:
            return WA, execute_time, different_length_message(answer_length, user_length)

        #  different lines
        for index, lines in enumerate(zip(answer, user)):
            answer_line, user_line = lines
            if answer_line != user_line:
                return WA, execute_time, different_lines_message(answer_line, user_line, index)

        # time limit
        if execute_time > self.time_limit:
            return TL, execute_time, time_limit_message(self.time_limit)

        #  all is correct
        return SC, execute_time, ''
