from tester import ScriptTester, rb_file

CMD = "python running_file.py"
TEST = "archive_9-11\\5\\tests\\01"


def main():
    tester = ScriptTester(CMD)

    stdout, stderr, execute_time = tester.execute(rb_file("input.txt"))
    print(stdout)
    print(stderr)
    print(execute_time)

    stdout, stderr, execute_time = tester.execute(rb_file("input.txt"))
    print(stdout)
    print(stderr)
    print(execute_time)


if __name__ == '__main__':
    main()
