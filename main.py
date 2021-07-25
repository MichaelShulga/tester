import subprocess


LANG = "python"
FILE = "running_file.py"
TEST = "archive_9-11\\5"


def main():
    task = subprocess.Popen([LANG, FILE], stdin=subprocess.PIPE)
    task.communicate(b'test2')


if __name__ == '__main__':
    main()
