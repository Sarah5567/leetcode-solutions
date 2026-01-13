class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double left = squares[0][1], right = squares[0][1];
        for(auto& square : squares){
            int y = square[1], l = square[2];
            left = min(left, (double)y);
            right = max(right, (double)(y + l));
        }

        double mid;
        for (int it = 0; it < 80 && right - left > 1e-7; it++) {
            mid = left + (right - left) / 2.0;
            double above = 0, bellow = 0;

            for(auto& square : squares){
                double y = square[1], l = square[2];
                above += max(0.0, y + l - max(mid, y)) * l;
                bellow += max(0.0, min(mid, y + l) - y) * l;
            }

            if(above > bellow)
                left = mid;
            else
                right = mid;
        }
        return mid;
    }
};