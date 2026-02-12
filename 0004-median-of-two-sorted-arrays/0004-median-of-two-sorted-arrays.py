class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = total_left - i      # Partition index for nums2
            
            # Boundary values (handle out-of-bounds with infinity)
            leftA = nums1[i-1] if i > 0 else float('-inf')
            rightA = nums1[i] if i < m else float('inf')
            leftB = nums2[j-1] if j > 0 else float('-inf')
            rightB = nums2[j] if j < n else float('inf')
            
            # Check if partition is valid
            if leftA <= rightB and leftB <= rightA:
                # Even total elements
                if (m + n) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                # Odd total elements
                else:
                    return max(leftA, leftB)
            
            # If leftA is too big, move i to the left
            elif leftA > rightB:
                high = i - 1
            # If leftB is too big, move i to the right
            else:
                low = i + 1