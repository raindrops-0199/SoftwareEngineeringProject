from InFile import InFile
from Judger import Judger

if __name__ == '__main__':
    path = "../input/50A"
    infile = InFile(path)
    infile.read_folder()
    infile.parse_stdin()
    judge = Judger(infile)
    judge.judge()
    judge.write_out()
