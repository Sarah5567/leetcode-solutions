class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        int n = words.size(), len = words[0].size();
        vector<int> res;

        unordered_map<string_view, int> freq;
        freq.reserve(words.size());
        for (auto& w : words) freq[string_view(w)]++;

        for (int startPoint = 0; startPoint < len; startPoint++) {
            int curN = 0;
            unordered_map<string_view, int> curFreq;
            curFreq.reserve(freq.size());

            for (int i = startPoint; i + len <= (int)s.size(); i += len) {

                if (i - n * len >= 0) {
                    string_view removedWord(s.data() + (i - n * len), len);
                    auto itRem = freq.find(removedWord);
                    if (itRem != freq.end()) {
                        int &cnt = curFreq[removedWord];
                        if (cnt <= itRem->second) curN--;
                        cnt--;
                    }
                }

                string_view curWord(s.data() + i, len);
                auto it = freq.find(curWord);
                if (it != freq.end()) {
                    int &cnt = curFreq[curWord];
                    cnt++;
                    if (cnt <= it->second) curN++;
                }

                if (curN == n) res.push_back(i - (n - 1) * len);
            }
        }

        return res;
    }
};
