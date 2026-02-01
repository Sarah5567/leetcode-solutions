class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
            vector<int> freq(26, 0);

            for (char ch : tasks)
                freq[ch - 'A']++;
            
            queue<pair<int,int>> q;
            priority_queue<int> pq;
            for(auto f : freq){
                if(f){
                    pq.push(f);
                }
            }

            int idx = 0;
            while(!pq.empty() || !q.empty()){
                if(!q.empty() && (q.front().first <= idx || pq.empty())){
                    pq.push(q.front().second);
                    if(q.front().first > idx){
                        idx = q.front().first;
                    }

                    q.pop(); 
                }

                int max_freq = pq.top();
                max_freq--;
                if(max_freq){
                    q.push({idx + n + 1, max_freq});
                }
                
                pq.pop();
                idx++;
            }

            return idx;
    }
};