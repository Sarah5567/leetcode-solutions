class Solution {
public:
    int searchCycle(vector<vector<pair<int, int>>>& adj, vector<bool>& visited, int node){
        visited[node] = true;
        for(auto v : adj[node]){
            if(visited[v.first])
                return v.first;
            else{
                int ans = searchCycle(adj, visited, v.first);
                if(ans != -1)
                    return ans;
            }
        }
        visited[node] = false;
        return -1;
    }
    int findEdge(vector<vector<pair<int, int>>>& adj, vector<bool>& visited, int node){
        visited[node] = true;
        for(auto v : adj[node]){
            if(visited[v.first])
                return v.second;
            else{
                int ans = findEdge(adj, visited, v.first);
                if(ans != -1)
                    return max(ans, v.second);
            }
        }
        return -1;
    }
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        //count number of nodes
        int n = 0;
        for(auto edge : edges)
            n = max(n, max(edge[0], edge[1]));

        n++;

        vector<vector<pair<int, int>>> outEdges(n);
        vector<vector<pair<int, int>>> inEdges(n);
        for(int i = 0; i < edges.size(); i++){
            outEdges[edges[i][0]].push_back({edges[i][1], i});
            inEdges[edges[i][1]].push_back({edges[i][0], i});
        }

        auto targetNode = find_if(inEdges.begin(), inEdges.end(), [](vector<pair<int, int>> v){
            return v.size() == 2;
        });

        vector<bool> visited(n, false);
        if(targetNode != inEdges.end()){
            auto op1 = (*targetNode)[0];
            auto op2 = (*targetNode)[1];
            if(searchCycle(outEdges, visited, op1.first) == op1.first)
                return edges[op1.second];
            visited.assign(n, false);
            if(searchCycle(outEdges, visited, op2.first) == op2.first)
                return edges[op2.second];
            return edges[max(op1.second, op2.second)];
        }

        //looking for node to begin the search for cycle from
        //if there is node which is not parent of any other node, it can be the first
        //otherwise, all the graph is one cycle
        int beginNode;
        for(beginNode = 1; beginNode < n && !(outEdges[beginNode].empty()); beginNode++);

        int nodeInCycle = 1;
        if(beginNode != n){
            //search in invert graph, from starting from leaf node which is root
            //in invert graph
            nodeInCycle = searchCycle(inEdges, visited, beginNode);
        }
        visited.assign(n, false);
        return edges[findEdge(outEdges, visited, nodeInCycle)];
    }
};