class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # 紀錄 fast slow 第一次相遇index
        while (slow==0 and fast ==0) or slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        index = fast

        # 開始查詢第一次重複點
        slow = 0
        while slow != index:
            slow = nums[slow]
            index = nums[index]
        return slow