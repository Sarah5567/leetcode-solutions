class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
            int n = words.size(), len = words[0].size();
            vector<int> res;

            unordered_map<string,int> freq;
            for (auto& word : words) freq[word]++;
  
            for(int startPoint = 0; startPoint < len; startPoint++){
                int curN = 0;
                unordered_map<string,int> curFreq;
                for (const auto& [word, frequency] : freq) curFreq[word] = 0;

                for(int i = startPoint; i + len <= s.size(); i += len){
                    if(i - n * len >= 0){
                        string removedWord = s.substr(i - n * len, len);

                        if(curFreq.find(removedWord) != curFreq.end()){
                            if(curFreq[removedWord] <= freq[removedWord])
                                curN -= 1;
                            curFreq[removedWord] -= 1;
                        }
                    }

                    string curWord = s.substr(i, len);
                    if(curFreq.find(curWord) != curFreq.end()){
                        curFreq[curWord] += 1;

                        if(curFreq[curWord] <= freq[curWord])
                            curN += 1;
                    }

                    if(curN == n) res.push_back(i - (n - 1) * len);
                }

            }
            return res;
    }
};