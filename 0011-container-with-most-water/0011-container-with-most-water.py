class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers
        left, right = 0, len(height) - 1
        out = 0
        
        while left < right:
            if height[left] < height[right]:
                out = max(out, (right - left) * height[left])
                left += 1
            else:
                out = max(out, (right - left) * height[right])
                right -= 1
            
        return out