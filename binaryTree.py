class BinTree:
    def __init__(self, data:list):
        self.data = data

    def add(self, number):
        pass      

    def contains(self, number):       
        first_element = 0
        last_element = len(self.data) - 1

        while(first_element <= last_element): 
            mid_element = int((first_element + last_element) / 2)

            if number == self.data[mid_element]:
                return True           
            elif number < self.data[mid_element]:
                last_element = mid_element - 1           
            else:
                first_element = mid_element + 1 
        
        return False