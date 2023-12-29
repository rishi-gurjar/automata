import random

class Cellular:
    def setArray(self, chosen_col, rows, cols):
        assert isinstance(chosen_col, int) and chosen_col > 0 and chosen_col <= cols, "Invalid selected column"

        self.array = [[False] * cols] * rows
        self.array[0][chosen_col - 1] = True # Set initial cell
    
    def updateLifeform(self, index):
        if index not in self.lifeform and index is not None:
            self.lifeform.append(index)
    
    def __init__(self, chosen_col, rows=1, cols=5, epochs=5):
        assert epochs > 2, "# of Epochs are too low"

        self.deadforms = []
        self.lifeform = [chosen_col - 1]
        self.setArray(chosen_col, rows, cols)
        self.evolution(epochs)

    def showArray(self):
        for row in self.array:
            print(row) 
            
    def dynamics(self):
        self.underpopulation()
        self.overpopulation()
        self.mating()
    
    def overpopulation(self):
        index = 1
        copy = self.array[0][:]
        for col in copy[1:]:
            if col == True and index <= len(self.array[0]) - 2:
                #print(col, index)
                if self.array[0][index - 1] == True and self.array[0][index + 1] == True:
                    self.array[0][index] = False
                    self.lifeform.remove(index)
                    self.deadforms.append(index)
            index+=1

    def underpopulation(self):
        index = 1
        copy = self.array[0][:]
        for col in copy[1:]:
            if col == True and index <= len(self.array[0]) - 2:
                #print(col, index)
                if self.array[0][index - 1] == False and self.array[0][index + 1] == False:
                    self.array[0][index] = False
                    self.lifeform.remove(index)
                    self.deadforms.append(index)
            index+=1

    def mating(self):
        index = 0
        for col in self.array[0]:
            if col == False:
                if index not in self.deadforms:
                    self.deadforms.append(index)
            index+=1
        #print('Deadforms', self.deadforms)
                    
        for deadform in self.deadforms:
            if deadform - 1 >= 0 and deadform < len(self.array[0]) - 1:
                if deadform - 1 in self.lifeform and deadform + 1 in self.lifeform:
                    self.array[0][deadform] = True

                    self.updateLifeform(deadform)
                    self.deadforms.remove(deadform)
            else:
                pass                
        
    
    def spontaneous_reproduction(self): # SPONTANEOUS LIFE 
        random_col = random.randint(1,len(self.array[0])) 
        self.array[0][random_col - 1] = True
        self.updateLifeform(random_col - 1)

    def reproduction(self): # REPRODUCES
        for col_index in range(1, len(self.array[0])): # iterating through columns
            if col_index < 1:
                if self.array[0][col_index - 1] == 1 and self.array[0][col_index + 1] == 1 and self.array[0][col_index + 2] == 1:
                    self.array[0][col_index] = 1
            else:
                if self.array[0][col_index - 1] == 1 and self.array[0][col_index - 2] == 1 and self.array[0][col_index + 1] == 1 \
                or self.array[0][col_index - 1] == 1 and self.array[0][col_index + 1] == 1 and self.array[0][col_index + 2] == 1:
                    self.array[0][col_index] = 1

    def binary_fission(self):
        for life in self.lifeform:
            if life > 0 and self.array[0][life - 1] == False:
                self.array[0][life - 1] = True
                return life - 1

    def evolution(self, epochs):
        self.showArray() # init array
        #print("Lifeforms", self.lifeform)
        for _ in range(2):
            self.spontaneous_reproduction() # 2 spontaneous epochs
            self.showArray()
            #print("Lifeforms", self.lifeform)

        for _ in range(epochs - 2): # (epochs - 2) epochs
            self.dynamics()
            self.showArray()

            #print("Lifeforms", self.lifeform)

cellular_instance = Cellular(chosen_col=5, cols=10, epochs=10)
