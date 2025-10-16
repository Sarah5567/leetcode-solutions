class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> um;
        int longest = 0, lastRepitition = -1;
        for (int i = 0; i < s.length(); i++){
            auto it = um.find(s[i]);
            int prevIndex = -1;
            if (it != um.end()){
                prevIndex = it->second;
                lastRepitition = max(lastRepitition, prevIndex);
            }
            um[s[i]] = i;
            int curSubstring = i - lastRepitition;
            longest = max(longest, curSubstring);
        }

        return longest;
    }
};