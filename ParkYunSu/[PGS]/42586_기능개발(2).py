import math
from collections import deque

class sechedule():
    def __init__(self, progresses, speeds):
        self.progresses = progresses
        self.speeds = speeds
        self.deploy = self.cal_day()

    def cal_day(self):
        return deque([math.ceil((100 - x) / y) for x, y in zip(self.progresses, self.speeds)])
    
    def manage_sechdule(self):
        answer = []
        while self.deploy:
            deploy_day = self.deploy.popleft()
            count = 1
            while self.deploy and self.deploy[0] <= deploy_day:
                self.deploy.popleft()
                count += 1
            answer.append(count)

        return answer

def solution(progresses, speeds):
    answer = sechedule(progresses, speeds)
    return answer.manage_sechdule()

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))

    progresses2 = [95, 90, 99, 99, 80, 99]
    speeds2 = [1, 1, 1, 1, 1, 1]
    print(solution(progresses2, speeds2))