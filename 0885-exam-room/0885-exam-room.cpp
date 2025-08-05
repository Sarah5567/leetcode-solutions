#include <unordered_map>
#include <utility>
#include <queue>
#include <vector>
using namespace std;
using int_pair = pair<int, int>;

class ExamRoom {
private:
    class Compare{
       int n;
    public:
        Compare(int n): n(n) {}
        int dist(const int_pair& p){
            if(p.first == -1)
                return p.second;
            else if (p.second == n)
                return n - 1 - p.first;
            else
                return (p.second - p.first) / 2;
        }
        bool operator()(const int_pair& a, const int_pair& b){
            int distA = dist(a);
            int distB = dist(b);
            if(distA == distB)
                return a.first > b.first;
            return distA < distB;
        }
    };
    priority_queue<int_pair, vector<int_pair>, Compare> heap;
    unordered_map<int, int_pair> starts;
    unordered_map<int, int_pair> ends;
    int n;
    
    void add_interval(int left, int right){
        if(left < right){
            heap.emplace(left, right);
            starts[left] = {left, right};
            ends[right] = {left, right};
        }
    }
    
public:
    ExamRoom(int n) :n(n), heap(Compare(n)) {
        add_interval(-1, n);
    }
    
    int seat() {
        while(!heap.empty()){
            auto [left, right] = heap.top();
            heap.pop();
            
            if(starts.find(left) == starts.end() || starts[left].second != right)
                continue;
            
            starts.erase(left);
            ends.erase(right);
            
            int seat;
            if(left == -1)
                seat = 0;
            else if(right == n)
                seat = n - 1;
            else
                seat = left + (right - left) / 2;
                
            add_interval(left, seat);
            add_interval(seat, right);
            return seat;
        }
        return -1;
    }
    
    void leave(int p) {
        if(ends.find(p) == ends.end() || starts.find(p) == starts.end())
            return;
        int_pair left_interval = ends[p];
        int_pair right_interval = starts[p];
        
        int new_left = left_interval.first;
        int new_right = right_interval.second;
        
        starts.erase(left_interval.first);
        ends.erase(left_interval.second);
        
        starts.erase(right_interval.first);
        ends.erase(right_interval.second);
        
        add_interval(new_left, new_right);
    }
};
