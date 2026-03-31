class Solution(object):
    def topKFrequent(self, nums, k):
        frequencyMappy = {}
        for currentNumber in nums:
            if currentNumber in frequencyMappy:
                frequencyMappy[currentNumber] += 1
            else:
                frequencyMappy[currentNumber] = 1
        bucketList = []
        # create list of list
        for i in range(len(nums) + 1):
            bucketList.append([])
        #
        for num, freq in frequencyMappy.items():
            bucketList[freq].append(num)
        result = []
        for i in range(len(bucketList)-1, 0, -1):
            for num in bucketList[i]:
                result.append(num)
                if len(result) == k:
                    return result