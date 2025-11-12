#include <string>
#include <vector>
#include <unordered_set>
#include <sstream>
#include <string_view>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string replaceWords(const vector<string>& dictionary, const string& sentence) {
        unordered_set<string_view> roots;
        roots.reserve(dictionary.size());
        for (const auto& root : dictionary)
            roots.insert(root);

        istringstream iss(sentence);
        string word;
        string result;
        result.reserve(sentence.size());

        unordered_map<string, string> cache;
        cache.reserve(64);

        bool first = true;
        while (iss >> word) {
            if (!first)
                result.push_back(' ');
            else
                first = false;

            auto it = cache.find(word);
            if (it != cache.end()) {
                result.append(it->second);
                continue;
            }

            int len = 1;
            int wordSize = word.size();
            for (; len <= wordSize && !roots.contains(string_view(word).substr(0, len)); ++len);

            string_view replacement = (len <= wordSize)
                                          ? string_view(word).substr(0, len)
                                          : string_view(word);
            cache.emplace(word, string(replacement));
            result.append(replacement);
        }

        return result;
    }
};
