class Solution {
private:
    long long gcd(long long a, long long b) {
        while (b != 0) {
            long long t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    pair<long long, long long> getNormalizedSlope(long long dx, long long dy) {
        if (dx == 0) return {1, 0};
        if (dy == 0) return {0, 1};
        if (dx < 0) { dx = -dx; dy = -dy; }
        long long g = gcd(dx, dy);
        return {dy / g, dx / g};
    }

public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();

        unordered_map<long long, unordered_map<long long, int>> dummy; // dummy for type
        unordered_map<long long, unordered_map<long long, int>> dictHash;
        unordered_map<long long, unordered_map<long long, unordered_map<long long, int>>> midpointsHash;

        auto pairHash = [](const pair<long long,long long>& p) -> long long {
            return p.first * 1000000007LL + p.second;
        };

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long long dx = points[j][0] - points[i][0];
                long long dy = points[j][1] - points[i][1];

                auto slope = getNormalizedSlope(dx, dy);
                long long hSlope = pairHash(slope);

                long long C = slope.first * points[i][0] - slope.second * points[i][1];
                dictHash[hSlope][C]++;

                long long midX2 = points[i][0] + points[j][0];
                long long midY2 = points[i][1] + points[j][1];
                midpointsHash[midX2][midY2][hSlope]++;
            }
        }

        long long totalParallelPairs = 0;
        for (auto& [slope, c_map] : dictHash) {
            long long currentSlopeTotalSegments = 0;
            for (auto& [c_val, count] : c_map)
                currentSlopeTotalSegments += count;

            for (auto& [c_val, count] : c_map) {
                currentSlopeTotalSegments -= count;
                totalParallelPairs += (long long)count * currentSlopeTotalSegments;
            }
        }

        long long parallelograms = 0;
        for (auto& [x, y_map] : midpointsHash) {
            for (auto& [y, slope_map] : y_map) {
                long long runningSum = 0;
                for (auto& [slope, count] : slope_map) {
                    parallelograms += (long long)count * runningSum;
                    runningSum += count;
                }
            }
        }

        return (int)(totalParallelPairs - parallelograms);
    }
};
