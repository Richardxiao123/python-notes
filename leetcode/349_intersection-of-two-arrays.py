class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=set()
        nums1.sort()
        nums2.sort()
        i,j=0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j]:
                intersection.add(nums1[i])
                i+=1
                j+=1

            elif nums1[i] > nums2[j]:
                j += 1

            elif nums2[j] > nums1[i]:
                i += 1

        
        return [*intersection]
