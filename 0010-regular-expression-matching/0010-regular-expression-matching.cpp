class Solution {
public:
    vector<string> parsePatternIntoVector(string p){
        vector<string> vec(p.size(), "");
        int vec_index = 0;

        for(int i = 0; i < p.size(); i++){
            if(p[i] != '*')
                vec[vec_index++] += p[i];
            else if (p[i - 1] != '*')
                vec[vec_index - 1] += p[i];
        }

        vec.resize(vec_index);
        return vec;
    }

    bool isMatch(string s, string p) {
        vector<string> p_vec = parsePatternIntoVector(p);
        
        vector<vector<bool>> dp(p_vec.size() + 1, vector<bool>(s.length() + 1, false));

        //if both p_vec and s are empty, answer should be true
        dp[0][0] = true;
        for(int i = 1; i <= p_vec.size() && p_vec[i - 1].size() == 2; i++)
            dp[i][0] = true;

        for(int i = 1; i <= p_vec.size(); i++){
            for(int j = 1; j <= s.length(); j++){
                if(p_vec[i - 1][0] == s[j - 1] || p_vec[i - 1][0] == '.'){
                    dp[i][j] = dp[i - 1][j - 1];
                    if(p_vec[i - 1].length() == 2)
                        dp[i][j] = dp[i][j] | dp[i][j - 1];
                }
                if(p_vec[i - 1].length() == 2)
                        dp[i][j] = dp[i][j] | dp[i - 1][j];
            }
        }

        return dp[p_vec.size()][s.length()];
    }
};