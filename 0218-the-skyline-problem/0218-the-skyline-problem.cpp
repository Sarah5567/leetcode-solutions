#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> events;
        // create events: start -> positive height, end -> negative height
        for (auto& b : buildings) {
            events.push_back({b[0], -b[2]}); // start
            events.push_back({b[1],  b[2]}); // end
        }

        // sort events: by x, then by height
        sort(events.begin(), events.end(), [](auto& a, auto& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });

        multiset<int> heights = {0}; // keep current active heights
        int prevMax = 0;
        vector<vector<int>> res;

        for (auto& e : events) {
            int x = e.first, h = e.second;
            if (h < 0) {
                // start of building
                heights.insert(-h);
            } else {
                // end of building
                heights.erase(heights.find(h));
            }

            int curMax = *heights.rbegin();
            if (curMax != prevMax) {
                res.push_back({x, curMax});
                prevMax = curMax;
            }
        }

        return res;
    }
};
