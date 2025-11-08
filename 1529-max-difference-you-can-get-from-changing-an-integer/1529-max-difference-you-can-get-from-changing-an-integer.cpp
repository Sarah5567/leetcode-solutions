class Solution {
public:
    int proccessNum(int num, int x, int y){
        int newNum = 0, pow = 1;
        while(num){
            int digit = num % 10;
            if(digit == x)
                digit = y;
            
            newNum += digit * pow;
            pow *= 10;
            num /= 10;
        }

        return newNum;
    }
    int maxDiff(int num) {
        int xForLarge = num % 10, xForSmall = num % 10;
        bool beginWith1;
        int temp = num;

        while(temp){
            if(temp % 10 < 9)
                xForLarge = temp % 10;
            if(temp % 10 > 1)
                xForSmall = temp % 10;
            if(temp % 10 == temp)
                beginWith1 = temp == 1;
            temp /= 10;
        }

        return proccessNum(num, xForLarge, 9) - proccessNum(num, xForSmall, !beginWith1 || xForSmall == 1);
    }
};