class Obj:
    def __init__(self, x):
        self.x = x

    # def __eq__(self, value):
    #     return self.x == value.x

    def __hash__(self):
        return hash(self.x)
    
    def __str__(self):
        return f"Obj: {self.x}"
    
    

from collections import Counter
c = Counter()
c[Obj(1)] += 1
c[Obj(1)] += 1
c[Obj(2)] += 1

for item in c:
    print(f"{item} = {c[item]}")
