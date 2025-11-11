class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        return floor((-1 + sqrt(1 + 8 * grades.size())) / 2);

    }
};