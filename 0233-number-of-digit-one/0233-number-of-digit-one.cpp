#include <cmath>

class Solution {
public:
    int countDigitOne(int n) {
        int count = 0, partial_n = 0, mask = 1;

        while(n){
            count += (n / 10 + (n % 10 > 1)) * mask;
            if(n % 10 == 1){
                count += partial_n + 1;
            }

            partial_n += (n % 10) * mask;
            n /= 10;
            if(n)
                mask *= 10;
        }
        return count;
    }
};