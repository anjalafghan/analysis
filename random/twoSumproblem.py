from typing import List, Self

target = 6
numberList = [3,2,4]

class Solution:
    def twosum(self, numberList: List[int], target: int):
        dictionary = {}
        length = len(numberList)
        for i in range(length):
            compliment = target - numberList[i]
            if compliment in dictionary:
                return [dictionary[compliment],i]
            dictionary[numberList[i]] = i
        return []
answer = Solution.twosum(Self, target=target, numberList=numberList)
print(answer)