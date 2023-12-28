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
        self.lifeform = [chosen_col - 1]
        self.setArray(chosen_col, rows, cols)
        self.evolution(epochs)

    def showArray(self):
        for row in self.array:
            print(row) 
            
    def dynamics(self):
        lifeform_indexes = []
        for life in self.lifeform:
            count = 0
            if life > 0 and self.array[0][life - 1] == True:
                count+=1
            if life > 1 and self.array[0][life - 2] == True:
                count+=1
            if life < len(self.array[0]) - 1 and self.array[0][life + 1] == True:
                count+=1
            if life < len(self.array[0]) - 2 and self.array[0][life + 2] == True:
                count+=1

            if count < 2:
                random_col = random.randint(1,len(self.array[0])) # SPONTANEOUS LIFE 
                self.array[0][random_col - 1] = True
                #self.array[0][life] == False # UNDERPOPULATION
                lifeform_indexes.append(random_col - 1)
                print('rand!')
            elif count > 3:
                self.array[0][life] == False # OVERPOPULATION
                lifeform_indexes.remove(life)
            else:
                self.array[0][life] == True # MATING
                lifeform_indexes.append(life)
        
        return lifeform_indexes
        #self.reproduction()

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
        for _ in range(epochs):
            self.showArray()
            lifeform_indexes = self.dynamics()
            
            for index in lifeform_indexes:
                self.updateLifeform(index)

            #lifeform_index = self.binary_fission()
            #print("Lifeforms", self.lifeform)


cellular_instance = Cellular(3)
