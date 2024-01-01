from collections import defaultdict


class Solution:
    def sift(self, low, high):
        i = low
        j = 2 * i + 1
        target = self.arr[low]
        while j <= high:
            if j + 1 <= high and self.num_record[self.arr[j + 1]] < self.num_record[self.arr[j]]:
                j += 1
            if self.num_record[target] > self.num_record[self.arr[j]]:
                self.arr[i] = self.arr[j]
                i = j
                j = 2 * i + 1
            else:
                break
        self.arr[i] = target

    def topKFrequent(self, nums, k):
        self.num_record = defaultdict(int)
        for num in nums:
            self.num_record[num] += 1

        self.arr = list(self.num_record.keys())
        for j in range((k - 1 - 1) // 2, -1, -1):
            self.sift(j, k - 1)
        for i in range(k, len(self.arr)):
            if self.num_record[self.arr[i]] > self.num_record[self.arr[0]]:
                self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
                self.sift(0, k - 1)
        return self.arr[:k]