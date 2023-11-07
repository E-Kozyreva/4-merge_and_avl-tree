class GenerateData:
    import random
    
    def __init__(self, n):
        self.array = []
        self.n = n
        
    def generate(self):
        for i in range(self.n):
            self.array.append(self.random.randint(0, 1_000_000))
        return self.array
