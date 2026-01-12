class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        auto maxCmp = [&](int i, int j) {
            return nums[i] < nums[j];
        };
        auto minCmp = [&](int i, int j) {
            return nums[i] > nums[j];
        };

        priority_queue<int, vector<int>, decltype(maxCmp)> maxHeap(maxCmp);
        priority_queue<int, vector<int>, decltype(minCmp)> minHeap(minCmp);

        vector<bool> isInMin(n, false);
        for(int i = 0; i < k; i++)
            maxHeap.push(i);
        for(int i = 0; i < k / 2; i++){
            minHeap.push(maxHeap.top());
            isInMin[maxHeap.top()] = true;
            maxHeap.pop();
        }

        int max_size = k - k / 2;
        int min_size = k / 2;
        vector<double> res(n - k + 1);

        res[0] = k % 2 ? nums[maxHeap.top()]
                    : ((double)nums[maxHeap.top()] + (double)nums[minHeap.top()]) / 2.0;

        for(int i = k; i < n; i++){
            int outIdx  = i - k;

            if(isInMin[outIdx]){
                while(!minHeap.empty() && minHeap.top() <= outIdx)
                    minHeap.pop();
                min_size -= 1; 
            }
            else{
                while(!maxHeap.empty() && maxHeap.top() <= outIdx)
                    maxHeap.pop();
                max_size -= 1; 
            }

            if(nums[i] <= nums[maxHeap.top()]){
                maxHeap.push(i);
                isInMin[i] = false;
                max_size += 1;
            }
            else{
                minHeap.push(i);
                isInMin[i] = true;
                min_size += 1;
            }

            if(min_size < k / 2){
                minHeap.push(maxHeap.top());
                isInMin[maxHeap.top()] = true;

                min_size += 1;
                max_size -= 1;

                maxHeap.pop();
                while(!maxHeap.empty() && maxHeap.top() <= outIdx)
                    maxHeap.pop();
            }
            else if(max_size < k - k / 2){
                maxHeap.push(minHeap.top());
                isInMin[minHeap.top()] = false;

                max_size += 1;
                min_size -= 1;

                minHeap.pop();
                while(!minHeap.empty() && minHeap.top() <= outIdx)
                    minHeap.pop();
            }

            res[i - k + 1] = k % 2 ? nums[maxHeap.top()]
                    : ((double)nums[maxHeap.top()] + (double)nums[minHeap.top()]) / 2.0;
        }

        return res;
    }
};