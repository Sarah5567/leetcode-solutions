class Solution {
    static void fixMax(const vector<vector<int>>& a, int& max1, int& max2) {
        if (a[max1].back() < a[max2].back()) std::swap(max1, max2);
    }
    static void fixMin(const vector<vector<int>>& a, int& min1, int& min2) {
        if (a[min1].front() > a[min2].front()) std::swap(min1, min2);
    }

public:
    int maxDistance(vector<vector<int>>& arrays) {
        int max1 = 0, max2 = 1;
        fixMax(arrays, max1, max2);

        int min1 = 0, min2 = 1;
        fixMin(arrays, min1, min2);

        for (int i = 2; i < (int)arrays.size(); ++i) {
            if (arrays[i].back() > arrays[max2].back()) {
                max2 = i;
                fixMax(arrays, max1, max2);
            }
            if (arrays[i].front() < arrays[min2].front()) {
                min2 = i;
                fixMin(arrays, min1, min2);
            }
        }

        if (max1 == min1) {
            return std::max(
                arrays[max1].back() - arrays[min2].front(),
                arrays[max2].back() - arrays[min1].front()
            );
        }
        return arrays[max1].back() - arrays[min1].front();
    }
};
