class Solution {
private:
    long long gcd(long long a, long long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    pair<long long, long long> getNormalizedSlope(long long dx, long long dy) {
        if (dx == 0) return {1, 0};
        if (dy == 0) return {0, 1}; 
        if (dx < 0) { dx = -dx; dy = -dy; } 
        long long common = gcd(abs(dx), abs(dy));
        return {dy / common, dx / common};
    }

public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        
        map<pair<long long, long long>, map<long long, int>> dict;
        
        map<pair<int, int>, map<pair<long long, long long>, int>> midpoints;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long dx = points[j][0] - points[i][0];
                long long dy = points[j][1] - points[i][1];
                
                pair<long long, long long> slope = getNormalizedSlope(dx, dy);
                
                long long C = (long long)slope.first * points[i][0] - (long long)slope.second * points[i][1];
                
                dict[slope][C]++;

                // נקודת אמצע (מוכפלת ב-2 למניעת double)
                int midX2 = points[i][0] + points[j][0];
                int midY2 = points[i][1] + points[j][1];
                midpoints[{midX2, midY2}][slope]++;
            }
        }

        long long totalParallelPairs = 0;
        for (auto& [slope, c_map] : dict) {
            long long currentSlopeTotalSegments = 0;
            for (auto& [c_val, count] : c_map) {
                currentSlopeTotalSegments += count;
            }
            
            for (auto& [c_val, count] : c_map) {
                currentSlopeTotalSegments -= count;
                totalParallelPairs += (long long)count * currentSlopeTotalSegments;
            }
        }

        long long parallelograms = 0;
        for (auto& [mid, slope_counts] : midpoints) {
            long long runningSum = 0;
            for (auto& [slope, count] : slope_counts) {
                parallelograms += (long long)count * runningSum;
                runningSum += count;
            }
        }

        return (int)(totalParallelPairs - parallelograms);
    }
};