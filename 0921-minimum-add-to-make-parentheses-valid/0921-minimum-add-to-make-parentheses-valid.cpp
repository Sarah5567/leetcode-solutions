class Solution {
public:
    int minAddToMakeValid(string s) {
        int balance = 0;
        int insertions = 0;

        for(auto& parenthesis : s){
            if(parenthesis == '('){
                balance++;
            }
            else{
                balance--;
                if(balance < 0){
                    insertions++;
                    balance++;
                }
            }
        }
        return insertions + balance;
    }
};