class EnterData:
    def __init__(self, str_nums):
        import re
        
        regex_num = re.compile('\d+')
        self.array = [int(n) for n in regex_num.findall(str_nums)]

    
class GenerateData:
    import random
    
    def __init__(self, n):
        self.array = []
        self.n = n
        
    def generate(self):
        for i in range(self.n):
            self.array.append(self.random.randint(0, 100_000))
        return self.array
    
    
class DataFromFile:
    def __init__(self, path):
        self.path = path
        self.array = []
        
    def read(self):
        with open(self.path, 'r') as f:
            for line in f:
                self.array.append(int(line))
        return self.array