class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min1 = INT_MIN, min2 = INT_MIN;
        int max1 = 0, max2 = 0;
        for(auto& price : prices){
            max2 = max(max2, price + min2);
            min2 = max(min2, max1 - price);
            max1 = max(max1, min1 + price);
            min1 = max(min1, -price);
        }
        return max2;
    }
};