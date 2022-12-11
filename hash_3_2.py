import time

# I have tested this with different kind of txt files and it works. (in this case there are so many words it will take approximately 93 years to find all matching values)


class RegularArray:  # initializing the array
    def __init__(self) -> None:
        self.array = []
        self.len = 0

    # insert the words from words_alpha to array with append
    def insert_to_array(self, file):
        f = open(file, "r")
        for line in f:
            self.array.append(line)
        self.len = len(self.array)

    def matching(self, file):  # gets second file and for each line in that file use search function which finds if any matching words are in the array
        count = 0
        f = open(file, "r")
        for line in f:

            if (self.search(line)):
                count += 1

        return count

    def search(self, data):  # searches from array and if any matches returns True else returns False so no matches
        for i in range(0, self.len):

            if self.array[i] == data:
                return True
        return False


if __name__ == "__main__":
    start = time.time()
    table = RegularArray()
    end = time.time()
    print("initializing time: ", end-start)
    start = time.time()
    table.insert_to_array("words_alpha.txt")
    end = time.time()

    print("time of inserting to hash table", end-start)
    start = time.time()
    print(table.matching("kaikkisanat.txt"))
    end = time.time()
    print("time of finding mathing words", end-start)
