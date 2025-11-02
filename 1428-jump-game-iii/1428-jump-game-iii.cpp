class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        if (n == 0) return false;

        vector<bool> isReached(n, false);
        queue<int> q;
        q.push(start);
        isReached[start] = true;

        while (!q.empty()) {
            int curIndex = q.front();
            q.pop();

            if (arr[curIndex] == 0)
                return true;

            int forwardJump = curIndex + arr[curIndex];
            if (forwardJump < n && !isReached[forwardJump]) {
                isReached[forwardJump] = true;
                q.push(forwardJump);
            }

            int backwardJump = curIndex - arr[curIndex];
            if (backwardJump >= 0 && !isReached[backwardJump]) {
                isReached[backwardJump] = true;
                q.push(backwardJump);
            }
        }

        return false;
    }
};
