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
        vector<vector<bool>> connections_mat(nodesNum, vector<bool>(nodesNum, false));
        for(auto pair : pairs){
            connections[pair[0]]++;
            connections[pair[1]]++;
            connections_mat[pair[0]][pair[1]] = true;
            connections_mat[pair[1]][pair[0]] = true;

        }
        int count_nodes = count_if(connections.begin(), connections.end(), [](int c){
            return c > 0;
        });

        int countRoots = count_if(connections.begin(), connections.end(), [count_nodes](int c){
            return c == count_nodes - 1;
        });

        if(!countRoots)
            return 0;
        bool foundMultiple = false;
        for(auto pair : pairs){
            if(connections[pair[0]] == connections[pair[1]])
                foundMultiple = true;
                
            int ancestor = pair[0];
            int descendant  = pair[1];
            if(connections[ancestor] < connections[descendant]){
                int temp = ancestor;
                ancestor = descendant;
                descendant = temp;
            }
            for(int i = 1; i < nodesNum; i++){
                if(connections_mat[descendant][i] && !(connections_mat[ancestor][i]) && i != ancestor)
                    return 0;
            }
            
        }
        if(foundMultiple)
            return 2;
        else
            return 1;
    }
};