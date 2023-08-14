class Solution:
    def __init__(self, api):
        self.api = api
        print('Press run code to see this in the console!')
        self.fieldSize = self.api.get_field_size()
        self.cows = self.api.get_number_of_cows()

    def create_cow_array(self):
        cowArray = [False] * (self.fieldSize * self.fieldSize)
        for i in range(self.cows):
            x = self.api.get_x_coordinate_for_cow(i)
            y = self.api.get_y_coordinate_for_cow(i)
            cowArray[y * self.fieldSize + x] = True
        return cowArray

    def get_neighbours(self, x, y):
        if self.fieldSize == 1:
            return []

        neighbours = []
        index = y * self.fieldSize + x

        if x == 0:
            neighbours.append(index + 1)
        elif x == self.fieldSize - 1:
            neighbours.append(index - 1)
        else:
            neighbours.extend([index - 1, index + 1])

        if y == 0:
            neighbours.append(index + self.fieldSize)
        elif y == self.fieldSize - 1:
            neighbours.append(index - self.fieldSize)
        else:
            neighbours.extend([index - self.fieldSize, index + self.fieldSize])

        return neighbours

    def get_number_of_cows_in_corners(self):
        if self.fieldSize == 1:
            return self.cows

        cowArray = self.create_cow_array()
        cornerIndexes = [
            0,
            self.fieldSize - 1,
            self.fieldSize * (self.fieldSize - 1),
            self.fieldSize * self.fieldSize
        ]
        count = sum(1 for index, cow in enumerate(cowArray) if index in cornerIndexes and cow)

        return count

    def get_number_of_cows_with_neighbours(self):
        cowArray = self.create_cow_array()
        count = 0

        for i in range(self.cows):
            x = self.api.get_x_coordinate_for_cow(i)
            y = self.api.get_y_coordinate_for_cow(i)

            neighbours = self.get_neighbours(x, y)
            count += sum(1 for index, cow in enumerate(cowArray) if index in neighbours and cow)

        return count