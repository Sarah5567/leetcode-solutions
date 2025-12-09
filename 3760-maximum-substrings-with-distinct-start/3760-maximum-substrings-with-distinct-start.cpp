class Solution {
public:
    int maxDistinct(string s) {
        constexpr int ALPHABET_SIZE = 26;
        vector<bool> letters(ALPHABET_SIZE, false);

        int count = 0;
        for(auto& ch : s){
            if(!letters[ch - 'a']){
                count++;
                letters[ch - 'a'] = true;
            }
        }
        return count;

    }
};