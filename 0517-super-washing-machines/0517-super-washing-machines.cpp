class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        long long sum = 0;
        int n = (int)machines.size();
        for (int x : machines) sum += x;

        if (sum % n != 0) return -1;
        long long avg = sum / n;

        long long balance = 0;
        long long ans = 0;

        for (int x : machines) {
            long long diff = x - avg;
            balance += diff;

            ans = max(ans, llabs(balance));
            ans = max(ans, diff);
        }

        return (int)ans;
    }
};
