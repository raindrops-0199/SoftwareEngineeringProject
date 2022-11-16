from InFile import InFile
from Judger import Judger


def main():
    path = "../input/50A"
    infile = InFile(path)
    infile.read_folder()
    infile.parse_stdin()
    judge = Judger(infile)
    judge.judge()
    judge.write_out()


if __name__ == '__main__':
    main()
