class balance():
    def __init__(self, s):
        self.s = s
        self.answer = 0
        
    def check(self):
        for x in self.s:
            self.answer += 1 if x == '(' else -1
            
            if self.answer < 0:
                return False
        return self.answer == 0
    
    def __repr__(self):
        return str(self.check())

def solution(s):
    return balance(s).check()

if __name__ == "__main__":
    s1 = "()()"
    s2 = "(()("
    print(balance(s1))
    print(balance(s2))