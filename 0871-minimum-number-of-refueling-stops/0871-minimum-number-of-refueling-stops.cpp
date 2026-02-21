class Solution {
private:
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> pq;
        int res = 0, i = 0;
        long long fuel = startFuel;

        while(fuel < target){
            while(i < stations.size() && stations[i][0] <= fuel){
                pq.push(stations[i][1]);
                i++;
            }
            if(pq.empty()) return -1;
            fuel += pq.top();
            pq.pop();
            res += 1;
        }
        return res;
    }
};