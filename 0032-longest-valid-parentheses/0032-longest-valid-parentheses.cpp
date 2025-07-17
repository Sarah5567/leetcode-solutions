class Solution {
public:
    int longestValidParentheses(string s) {
        std::stack<int> opening_parenthesises;
        int longest_parentheses = 0, begin_index = 0;;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '(')
                opening_parenthesises.push(i);
            else if(!(opening_parenthesises.empty())){
                opening_parenthesises.pop();
                if(!(opening_parenthesises.empty()))
                    longest_parentheses = max(longest_parentheses, i - opening_parenthesises.top());
                else
                    longest_parentheses = max(longest_parentheses, i + 1 - begin_index);

            }
            else
                begin_index = i + 1;
        }
        return longest_parentheses;
    }
};