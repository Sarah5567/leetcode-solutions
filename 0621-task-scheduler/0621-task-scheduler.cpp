class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
            int alphabet_size = 26;
            vector<int> freq(alphabet_size, 0);

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
                if(max_freq - 1){
                    q.push({idx + n + 1, max_freq - 1});
                }
                
                pq.pop();
                idx++;
            }

            return idx;
    }
};