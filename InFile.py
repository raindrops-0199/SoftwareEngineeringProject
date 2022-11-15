import os


class InFile:

    def __init__(self, path):
        self.folderPath = path
        self.in_format_name = "stdin_format.txt"
        self.inType = []
        self.inRange = []
        self.src_files = []

    def read_folder(self):
        files = os.listdir(self.folderPath)
        for file in files:
            if file != self.in_format_name and file != ".DS_Store":
                self.src_files.append(file)

    def parse_stdin(self):
        file = self.folderPath + "/" + self.in_format_name
        with open(file) as f:
            line = f.readline()
            while line:
                self.parse_line(line)
                line = f.readline()

    def parse_line(self, line):
        inputs = line.split(' ')
        for item in inputs:
            if item[0] == 'c':
                self.inType.append("char")
                self.inRange.append(range(0))
            else:
                start = item.find('(')
                end = item.find(',')
                range_start = int(item[start + 1:end])
                start = end
                end = item.find(')')
                range_end = int(item[start + 1:end])
                self.inRange.append(range(range_start, range_end))

                if item[0] == 'i':
                    self.inType.append("int")
                elif item[0] == 's':
                    self.inType.append("string")
