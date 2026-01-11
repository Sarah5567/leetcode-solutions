class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        for(int i = 2; i <= n; i++){
            string nextS = "";
            int count = 1;
            for(int j = 1; j < s.size(); j++){
                if(s[j] == s[j - 1])
                    count += 1;
                else{
                   nextS += count + '0';
                   nextS += s[j - 1];
                   count = 1;
                }
            }
            nextS += count + '0';
            nextS += s[s.size() - 1];
            s = nextS;
        }
        return s;
    }
};