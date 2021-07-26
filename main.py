from tester import ScriptTester, get_input

CMD = "python running_file.py"
TEST = "archive_9-11\\5\\tests\\01"


def main():
    tester = ScriptTester(CMD)

    stdout, stderr = tester.execute(get_input("input.txt"))
    print(stdout)
    print(stderr)

    stdout, stderr = tester.execute(get_input("input.txt"))
    print(stdout)
    print(stderr)


if __name__ == '__main__':
    main()
