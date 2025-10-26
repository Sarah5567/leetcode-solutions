class Solution {
public:
    int partitionString(string s) {
        vector<int> letters(26, -1);

        int substringBegin = 0, countSubstrings = 1;
        for(int i = 0; i < s.size(); i++){
            if(letters[s[i] - 'a'] >= substringBegin){
                substringBegin = i;
                countSubstrings++;
            }
            letters[s[i] - 'a'] = i;
        }

        return countSubstrings;
    }
};