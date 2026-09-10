class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        a = 1

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[a] = arr[i]
                a += 1
        return a