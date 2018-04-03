import sys #needed for Quit()
#task 1
class List1:
    def __init__(self, listy):
        pass
    #initializing class
    def __str__(self):
        self = str(self)
    #making a string version
    def __len__(self):
        self.length = len(self)
    #length of self
    def __contains__(self, item):
        for i in self:
            if self[i] == item:
                return True
            else:
                return False
    #search for item
    def __getitem__(self, index):
        return self[index]
    #return index
    def __setitem__(self, index, item):
        self[index] = item
        return slef[index]
    #set item at index
    def __eq__ (self, other):
        same = True
        for i in self:
            if self[i] != other[i]:
                same = False
    #checking if the lists are equal
    def append(self, item):
        return self.append(item)
    #appending new item to end of list
    def insert(self, index, item):
        for i in self:
            if i == index:
                self[i] = item
    #inserting item into list at specified point
    def remove(self, item):
        for i in self:
            if self[i] == item:
                self[i] = null
    # removing item at point
    def delete(self, index):
        self.pop(index)
    #delete item at point
    def sort(self, reverse):
        #blah
        pass
Listy=List1([3,4,5,6,4,5,2,3,4,6,7,8,5,4,3,3])


#task 2, makes list dynamic
lengthOfList = 20
listMade = []
for i in range(lengthOfList):
    listMade.append([])
print(listMade)
if listMade[19] != []:
    lengthOfList = 2*lengthOfList
    listMade1 = []*int(lengthOfList)
    listMade = listMade1 + listMade
    # if list is full, double

if listMade[4] == []:
    lengthOfList = 0.5*lengthOfList
    listMade1 = []*int(lengthOfList)
    listMade = listMade1 + listMade
    #if list is unused, halve


#task 3
def takeFileName(filename):
    filename = open(filename, 'r')
    read_data = filename.read()
    for i in filename:
        if read_data != '\n':
            listMade[i] = read_data
    filename.close()
    #reading data from file
takeFileName("hello.txt")
print(listMade)
#task 4
class Editor:
    
    def __init__(self, EditorList):
        self.EditorList = EditorList
        EditorList = []
    #initialization
    def insert_num(self,EditorList):
        self.EditorList = EditorList
        EditorList = []
        num = input("Please give a positive number")
        num = int(num)
        if num <= 0:
            print("?")
        text = input("Give a line of text please")
        EditorList.append([text])
        print(EditorList)
        Menu()
    #insert line
    def read_filename(self, EditorList):
        filename = input("Please enter filename")
        file = open(filename, 'r')
        read_data = file.read()
        for i in file:
            if read_data != '\n':
                EditorList[i] = read_data
        print(EditorList)
        file.close()
        Menu()
        #read a file
    def write_filename(self, EditorList):
        filename = input("Please enter filename")
        file = open(filename, 'w')
        for i in EditorList:
            file.write(i)
        file.close()
        Menu()
        #write a file
    def print_num1_num2(self,EditorList):
        num1 = input("Please enter num1")
        num2 = input("Please enter num2")
        num1 = int(num1)
        num2 = int(num2)
        if num1 < num2:
            diff = num2 - num1
            for i in range(num1, diff):
                print(EditorList[i])
        else:
            print("?")
        Menu()
    def delete_num(self, EditorList):
        num = input('Please ente a line to delete')
        num = int(num)
        if num != 0:
            EditorList.pop(num)
        else:
            EditorList = []
        Menu()
    def search_word(self, EditorList):
        counter = 0
        word = input("Please enter word to search for")
        for i in EditorList:
            if EditorList[i] == word:
                counter = counter + 1
        Menu()
    def quit(self):
        sys.exit()
    
EditorList = Editor([])
def Menu():
    print("There are many options. Please type one of the following:\n Insert Num\n Read\n Write\n Print\n Delete\n Search and count\n or Quit")
    selection = input()
    if selection == "Insert Num":
        EditorList.insert_num(EditorList)
    elif selection == "Read":
        EditorList.read_filename(EditorList)
    elif selection == "Write":
        EditorList.write_filename(EditorList)
    elif selection == "Print":
        EditorList.print_num1_num2(EditorList)
    elif selection == "Delete":
        EditorList.delete_num(EditorList)
    elif selection == "Search and count":
        EditorList.search_word(EditorList)
    elif selection == "Quit":
        EditorList.quit()
    else:
        print('Selection not recognised.')
Menu()



        
            
        
        
        
        
        

            
    
    
