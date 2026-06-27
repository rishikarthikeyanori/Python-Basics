# class Solution(object):
#     def containsDuplicate(self, nums):
#         arr=set()   
#         for i in nums:
#             if i in arr:
#                 return True
#             arr.add(i)
            
#         return False

            
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=s.sort()
        t=t.sort()
        if len(s.strip())!=len(t.strip()):
            return False

        if s.sort()!=t.sort():
            return False
        return True
    

            