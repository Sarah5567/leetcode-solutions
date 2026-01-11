class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        int left = 1;
        int right = position.back() - position.front();

        while(left < right){

            int mid = left + (right - left + 1) / 2;
            int difference = 0, reached = 1, last_position = position.front();

            for(int i = 1; i < position.size() && reached < m; i++){
                if(position[i] - last_position >= mid){
                    last_position = position[i];
                    reached += 1;
                }
            }

            if(reached < m)
                right = mid - 1;
            else
                left = mid;
        }

        return left;
    }
};