class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]  # Create a copy of nums1
        
        # Pointers for nums1_copy, nums2, and nums1
        p1 = 0
        p2 = 0
        p = 0
        
        # Compare elements from nums1_copy and nums2 and place them in nums1
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        
        # If there are any remaining elements in nums1_copy, copy them to nums1
        while p1 < m:
            nums1[p] = nums1_copy[p1]
            p1 += 1
            p += 1
        
        # If there are any remaining elements in nums2, copy them to nums1
        while p2 < n:
            nums1[p] = nums2[p2]
            p2 += 1
            p += 1
