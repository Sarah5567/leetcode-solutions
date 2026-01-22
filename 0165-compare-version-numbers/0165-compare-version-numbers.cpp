class Solution {
public:
    int compareVersion(string version1, string version2) {
        size_t begin1 = 0, begin2 = 0;
        size_t pos1 = 0, pos2 = 0;
        int num1, num2;
        int res = 0;

        while(pos1 < version1.size() && pos2 < version2.size() && !res){
            pos1 = version1.find('.', begin1);
            pos1 = (pos1 == string::npos) ? version1.size() : pos1;

            pos2 = version2.find('.', begin2);
            pos2 = (pos2 == string::npos) ? version2.size() : pos2;

            from_chars(version1.data() + begin1, version1.data() + pos1, num1);
            from_chars(version2.data() + begin2, version2.data() + pos2, num2);

            if(num1 > num2)
                res = 1;
            else if(num1 < num2)
                res = -1;

            begin1 = pos1 + 1;
            begin2 = pos2 + 1;
        }

        if(!res && pos1 < version1.size() && version1.find_first_not_of("0.", begin1) != string::npos)
            res = 1;
        else if(!res && pos2 < version2.size() && version2.find_first_not_of("0.", begin2) != string::npos)
            res = -1;

        return res;
    }
};