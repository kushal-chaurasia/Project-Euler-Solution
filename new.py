import traceback

def can_reach_end(nums):
    try:
        prev = 0
        for i in range(len(nums)):
            if i == 0:
                prev = nums[i]
                continue
            if nums[i] < nums[i +1] and nums
            if prev < nums[i]:
                return False
        return True
    except Exception as e:
        print(e)
        print(traceback.format_exc())

print(can_reach_end([1,2,3]))