import os

from tester import ScriptTester

CMD = "python running_file.py"
TESTS = "archive_9-11\\5\\tests"


def main():
    tester = ScriptTester(CMD)

    for filename in os.listdir(TESTS):
        if filename.endswith(".a"):
            print(os.path.join(TESTS, filename))

    with open("answer.txt", "rb") as f1:
        answer = f1.read()

    with open("input.txt", "rb") as f1:
        stdin = f1.read()

    verdict, execute_time, details = tester.test(stdin, answer)
    print(verdict)
    print(execute_time)
    print(details)


if __name__ == '__main__':
    main()
