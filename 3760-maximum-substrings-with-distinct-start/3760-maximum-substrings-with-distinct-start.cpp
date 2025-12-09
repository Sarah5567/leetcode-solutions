class Solution {
public:
    int maxDistinct(string s) {
        vector<bool> letters(26, false);
        int count = 0;
        for(auto& ch : s){
            if(!letters[ch - 'a'])
                count++;
            letters[ch - 'a'] = true;
        }
        return count;

    }
};