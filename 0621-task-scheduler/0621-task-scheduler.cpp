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

            int time = 0;
            while(!pq.empty() || !q.empty()){
                if(pq.empty()){
                    time = q.front().first;
                }

                if(!q.empty() && (q.front().first <= time || pq.empty())){
                    pq.push(q.front().second);
                    q.pop(); 
                }

                int max_freq = pq.top();
                if(--max_freq){
                    q.push({time + n + 1, max_freq});
                }
                
                pq.pop();
                time++;
            }

            return time;
    }
};