from InFile import InFile
from Judger import Judger
import os
import csv


def check(path):
    infile = InFile(path)
    infile.read_folder()
    infile.parse_stdin()
    judge = Judger(infile)
    judge.judge()
    judge.write_out()


def gen_output_file():
    fieldnames = ['file1', 'file2']
    with open("output/equal.csv", "w") as f1:
        writer = csv.writer(f1)
        writer.writerow(fieldnames)
    with open("output/inequal.csv", "w") as f2:
        writer = csv.writer(f2)
        writer.writerow(fieldnames)


def main():
    gen_output_file()
    root_path = "input"
    paths = os.listdir(root_path)
    for path in paths:
        if path != ".DS_Store":
            check(root_path + "/" + path)


if __name__ == '__main__':
    main()
