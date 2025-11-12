#include <string>
#include <vector>
#include <unordered_set>
#include <sstream>
using namespace std;

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        // שימוש ב-reserve כדי למנוע הקצאות חוזרות
        unordered_set<string> roots;
        roots.reserve(dictionary.size());
        for (const auto& root : dictionary)
            roots.insert(root);

        istringstream iss(sentence);
        string word;
        string result;
        result.reserve(sentence.size());

        bool first = true;
        while (iss >> word) {
            int len = 1;
            int wordSize = word.size();

            for (; len <= wordSize && !roots.contains(word.substr(0, len)); ++len);

            if (!first)
                result.push_back(' ');
            else
                first = false;

            if (len <= wordSize)
                result.append(word, 0, len);
            else
                result.append(word);
        }

        return result;
    }
};
