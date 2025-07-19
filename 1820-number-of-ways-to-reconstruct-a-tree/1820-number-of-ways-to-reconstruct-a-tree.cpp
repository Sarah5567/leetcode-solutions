#include <algorithm>
using namespace std;

class Solution {
public:
    int checkWays(vector<vector<int>>& pairs) {
        int nodesNum = 0;
        for(auto pair : pairs){
            nodesNum = max(nodesNum, pair[1]);
        }
        nodesNum++;

        vector<int> connections(nodesNum, 0);
        vector<vector<bool>> areConnected(nodesNum, vector<bool>(nodesNum, false));
        for(auto pair : pairs){
            connections[pair[0]]++;
            connections[pair[1]]++;
            areConnected[pair[0]][pair[1]] = true;
            areConnected[pair[1]][pair[0]] = true;

        }
        int countNodes = count_if(connections.begin(), connections.end(), [](int c){
            return c > 0;
        });

        int countRoots = count_if(connections.begin(), connections.end(), [countNodes](int c){
            return c == countNodes - 1;
        });

        if(!countRoots)
            return 0;
        bool foundMultiple = false;
        for(auto pair : pairs){                
            int ancestor = pair[0];
            int descendant  = pair[1];
            if(connections[ancestor] < connections[descendant])
                swap(ancestor, descendant);
            for(int i = 1; i < nodesNum; i++){
                if(areConnected[descendant][i] && !areConnected[ancestor][i] && i != ancestor)
                    return 0;
            }

            if(connections[pair[0]] == connections[pair[1]])
                foundMultiple = true;
        }
        if(foundMultiple)
            return 2;
        else
            return 1;
    }
};