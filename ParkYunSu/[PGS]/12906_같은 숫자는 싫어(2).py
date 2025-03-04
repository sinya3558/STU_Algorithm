class unique():
    def __init__(self, arr):
        self.arr = arr
        self.result = []

    def remove(self):
        for current in self.arr:
            if not self.result or self.result[-1] != current:
                self.result.append(current)
        return self.result

def solution(arr):
    answer = unique(arr)
    return answer.remove()

if __name__ == "__main__":
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution(arr))

    arr2 = [4, 4, 4, 3, 3]
    print(solution(arr2))