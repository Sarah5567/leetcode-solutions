class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> s;

        for (char ch : num) {
            while (!s.empty() && k > 0 && ch < s.top()) {
                s.pop();
                --k;
            }
            if (!s.empty() || ch != '0')
                s.push(ch);
        }

        while (!s.empty() && k > 0) {
            s.pop();
            --k;
        }

        if (s.empty()) return "0";

        string res(s.size(), '\0');
        for (int i = (int)res.size() - 1; i >= 0; --i) {
            res[i] = s.top();
            s.pop();
        }

        return res;
    }
};
