import csv
import string
from os import system
import random
import csv

class Judger:
    def __int__(self, infile):
        self.infile = infile
        self.equal = []
        self.unequal = []

    def judge(self):
        files = self.infile.src_files
        for i in range(len(files)):
            for j in range(i+1, len(files)):
                if self.compile(self.infile.path + '/' + files[i], 'a') and \
                        self.compile(self.infile.path + '/' + files[j], 'b'):
                    if self.is_equal():
                        self.equal.append([self.infile.path + '/' + files[i], self.infile.path + '/' + files[j]])
                        return
                self.unequal.append([self.infile.path + '/' + [i], self.infile.path + '/' + files[j]])
                return

    def compile(self, path, name):
        ret = system("g++ " + path + " -o " + name + " 2>&1")
        return ret == 0

    def is_equal(self):
        time = 10
        equal = True
        for i in range(time):
            self.generate_input()
            ret1 = system("./a < input.txt > output1.txt")
            ret2 = system("./b < input.txt > output2.txt")
            if ret1 != 0 or ret2 != 0:
                equal = False
                return equal
            equal = equal and self.is_output_same()

        return equal

    def generate_input(self):
        gen = []
        for i in range(len(self.infile.inType)):
            ty = self.infile.inType[i]
            ran = self.infile.inRange[i]
            if ty == "int":
                gen.append(random.randrange(ran[i].start, ran[i].stop))
            elif ty == "char":
                gen.append(random.choice(string.ascii_letters))
            else:
                to_add = ""
                length = random.randrange(ran[i].start, ran[i].stop)
                for j in range(length):
                    to_add += random.choice(string.ascii_letters)
                gen.append(to_add)

        with open("input.txt", "w") as f:
            to_write = " ".join(str(e) for e in gen)
            f.write(to_write)

    def is_output_same(self):
        f1 = open("output1.txt", "r")
        f2 = open("output2.txt", "r")
        res1 = f1.read()
        res2 = f2.read()
        f1.close()
        f2.close()
        return res1 == res2

    def write_out(self):
        fieldnames = ['file1', 'file2']
        with open("equal.csv", "w") as f1:
            writer = csv.writer(f1)
            writer.writerow(fieldnames)
            writer.writerows(self.equal)
            
        with open("inequal.csv", "w") as f2:
            writer = csv.writer(f2)
            writer.writerow(fieldnames)
            writer.writerows(self.unequal)
