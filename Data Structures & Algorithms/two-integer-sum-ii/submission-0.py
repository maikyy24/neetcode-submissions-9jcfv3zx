class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) -1 
        answer = [None] * 2
        while left < right :
            sum = numbers[left] + numbers[right]
            if sum == target : 
                answer[0] = left + 1 
                answer[1] = right + 1
                return answer
            if sum < target :
                left +=1
            else:
                right -=1
        