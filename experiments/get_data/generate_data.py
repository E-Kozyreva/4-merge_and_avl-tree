class GenerateData(object):
    import random
    
    def __init__(self, start: int, end: int, n: int):
        self.start = start
        self.end = end
        self.n = n
        self.array = []        
        

    def generate(self) -> list:
        for i in range(self.n):
            self.array.append(self.random.randint(self.start, self.end))
        return self.array
