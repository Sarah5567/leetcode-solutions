class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxAmount = 0;

        while(left < right){
            int amount = (right - left) * min(height[left], height[right]);
            maxAmount = max(maxAmount, amount);

            if(height[left] < height[right]) left++;
            else right--;
        }
        return maxAmount;
    }
};