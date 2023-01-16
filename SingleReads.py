def remove_common(list1, list2):  # Get unique values of 2 lists
    for i in list1[:]:
        if i in list2:
            list1.remove(i)
            list2.remove(i)
    return list1[0], list2[0]

class Single:

    # Class Variables
    path = ""
    lines = []
    kmer = 0
    from_seqs = []
    to_seqs = []
    cyclic_flag = False
    Sequence = ""

    def __init__(self, fpath):  # Class Constructor
        self.path = fpath

    def read_file(self):  # Reads each line in a file and put each one as en element of a list and gets length of 1 read
        with open(self.path) as file:
            for i, line in enumerate(file):
                if i != 0:
                    line = line.rstrip()
                    self.lines.append(line)
        self.kmer = len(self.lines[0])

    def create_path(self):  # Collect data of (k-mers - 1) from provided reads
        for i in range(len(self.lines)):
            self.from_seqs.append(self.lines[i][ : self.kmer-1])
            self.to_seqs.append(self.lines[i][1:])
        #return self.from_seqs, self.to_seqs

    def assemble(self):  # Create path and Assemble
        tempFrom = self.from_seqs.copy()
        tempTo = self.to_seqs.copy()
        uniques = list(remove_common(tempFrom, tempTo))
        unq_ind = self.from_seqs.index(uniques[0])
        self.Sequence += uniques[0] + self.to_seqs[unq_ind][-1]
        for i in self.from_seqs:
            if i == uniques[1]:
                self.cyclic_flag = True
        if self.cyclic_flag is False: # Handles non-cyclic case
            while True:
                if self.Sequence[-(self.kmer-1):] == uniques[1]:
                    break
                nextIndex = self.from_seqs.index(self.Sequence[-(self.kmer-1):])
                self.Sequence += self.to_seqs[nextIndex][self.kmer-2]
        else: # Handles cyclic case
            tfrom = self.from_seqs.copy()
            tto = self.to_seqs.copy()
            del tfrom[unq_ind]
            del tto[unq_ind]
            while True:
                nextIndex = tfrom.index(self.Sequence[-(self.kmer-1):])
                self.Sequence += tto[nextIndex][-1]
                del tfrom[nextIndex]
                del tto[nextIndex]
                if len(tfrom) == 0:
                   break
                #  C A G G G G A G G

    def predict(self):  # Runs the whole class functions in order and return the final required sequence
        self.read_file()
        self.create_path()
        self.assemble()
        return self.Sequence

if __name__ == "__main__":
    file = input("Enter file path: ")
    s = Single(file)
    output = s.predict()
    print("Your output is: ")
    print(output)
