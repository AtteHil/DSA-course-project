import time


class Node:
    def __init__(self, data) -> None:
        # initializing ndoe which have attributes data and next
        self.data = data
        self.next = None


class OpenHashing:
    def __init__(self, size) -> None:
        self.len = size
        # making the table of linked list start points with amount given. Initializing every node to None at start
        self.table = [Node(None) for i in range(size)]

    def hash_function(self, data):  # my hashing function
        sum = 0
        data = str(data)  # we make all string (in case it is integer or float)
        for i in range(len(str(data))):  # We go trough every letter in for loop
            sum += ord(data[i])  # sum their ascii values
        # make sum goes to power of so we get number big enough for larger hashing
        sum = (sum**2)-ord(data[0])
        # also minus the ascii value of first letter just to make sure two words doesn't come up with same sum
        return sum % self.len

    def search(self, data):  # search function searches from hash tables right slot with finding out hash value first
        slot = self.hash_function(data)
        node = self.table[slot]
        while node != None:  # while loop goes linked list trough and if there is searched value we return True and if not we return False
            if node.data == data:
                return True
            node = node.next
        return False

    def matching(self, file):  # finds matching values from given file and from hash table
        counter = 0
        f = open(file, "r")
        for line in f:
            if self.search(line) == True:
                counter += 1
        return counter  # returns how many words matched

    def insert_from_file(self, file):  # inserts words from given file to hash table
        f = open(file, "r")
        for line in f:
            self.insert(line)

    def insert(self, data):  # insert function receives data we want to insert
        new_node = Node(data)

        # calculates slot of the word or number
        slot = self.hash_function(data)
        node = self.table[slot]
        if node.data == None and node.data != data:  # if starting node is None
            self.table[slot] = new_node
            return
        else:
            while node != None:
                prev_node = node
                if node.data == data:  # sees if data is same we are trying to insert if it is returns print no duplicates
                    return print("No duplicates")
                node = node.next
            prev_node.next = new_node
        return

    def delete(self, data):
        # calculates where should the data we are trying to find is located(in whic of the linked lists)
        slot = self.hash_function(data)
        node = self.table[slot]

        prev = None
        if node.data == data:  # checks if it is the first node
            self.table[slot] = node.next
            node = None
            return True
        while node != None:  # goes trough linked list trying to find it
            if node.data == data:
                prev.next = node.next
                node = None
                return True  # if found it is deleted and set to None
            prev = node
            node = node.next
        return False  # if not found return False

    def printtable(self):  # Prints every value in hash table
        # takes one slot and in while loop goes trough it to to end printing every value in that Linked list
        print("Structure of the table: ")

        # for loop goes trough every starting point of linked lists
        for slot in range(self.len):
            print(slot, "[", end=" ")
            node = self.table[slot]
            while node != None:  # while loop goes trough every linked list and printing data
                print(node.data, end="; ")
                node = node.next
            print("]")


if __name__ == "__main__":
    start = time.time()
    table = OpenHashing(10000)
    end = time.time()
    print("initializing time: ", end-start)
    start = time.time()
    table.insert_from_file("words_alpha.txt")
    end = time.time()

    print("time of inserting to hash table", end-start)
    start = time.time()
    print(table.matching("kaikkisanat.txt"))
    end = time.time()
    print("time of finding mathing words", end-start)
