import os

from tester import ScriptTester, SC, WA, RE, TL

CMD = "python 5.py"
TESTS = "archive_9-11\\5\\tests"

DETAILS = False


def main():
    tester = ScriptTester(CMD)
    verdicts = {
        SC: "SC",
        WA: 'WA',
        RE: 'RE',
        TL: 'TL'
    }

    result = []
    for filename in os.listdir(TESTS):
        if '.' not in filename:  # no extension file matches input data
            with open(os.path.join(TESTS, filename), "rb") as f:
                stdin = f.read()
            with open(os.path.join(TESTS, filename + ".a"), "rb") as f:
                answer = f.read()

            verdict, execute_time, details = tester.test(stdin, answer)
            print('- ' * 7)
            print(verdicts[verdict], '\t', f'{round(execute_time * 100)}ms')
            print('- ' * 7)

            result.append(verdict)

    print()
    completed = result.count(SC) / len(result)
    print(f'{completed * 100}% completed successfully')

if __name__ == '__main__':
    main()
