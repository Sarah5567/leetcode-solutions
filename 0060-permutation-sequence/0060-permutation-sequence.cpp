class Solution {
public:
    string getPermutation(int n, int k) {
        int factorial = 1;
        string res, basic_res;
        for(int i = 1; i <= n; i++){
            factorial *= i;
            basic_res += i + '0';
        }

        k--;
        for(int i = n; i > 0; i--){
            factorial /= i;
            res += basic_res[k / factorial];
            basic_res.erase(k / factorial, 1);
            k %= factorial;
        }
        return res;
    }
};