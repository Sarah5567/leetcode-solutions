#include <queue>

class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(), courses.end(), [](vector<int> c1, vector<int> c2){
                    return c1[1] < c2[1];
        });
        priority_queue<int> pq;
        int total_time = 0, count_courses = 0;
        for(auto course : courses){
            pq.push(course[0]);
            total_time += course[0];
            if(total_time > course[1]){
                total_time -= pq.top();
                pq.pop();
            }
            else
                count_courses++;
        }
        return count_courses;
    }
};