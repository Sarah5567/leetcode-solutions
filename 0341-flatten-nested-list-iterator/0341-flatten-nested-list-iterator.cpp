class NestedIterator {
private:
    stack<pair<const vector<NestedInteger>*, int>> st;
    bool prepared = false;

    void moveToNextInteger() {
        while (!st.empty()) {
            auto &top = st.top();
            const auto *lst = top.first;
            int &idx = top.second;

            if (idx >= (int)lst->size()) {
                st.pop();
                if (!st.empty()) st.top().second++;
                continue;
            }

            if ((*lst)[idx].isInteger()) return;

            const auto &sub = (*lst)[idx].getList();
            st.push({&sub, 0});
        }
    }

    void prepare() {
        if (!prepared) {
            moveToNextInteger();
            prepared = true;
        }
    }

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        st.push({&nestedList, 0});
        prepared = false;
    }

    int next() {
        prepare();

        auto &top = st.top();
        int val = (*top.first)[top.second].getInteger();

        top.second++;
        prepared = false;
        return val;
    }

    bool hasNext() {
        prepare();
        return !st.empty();
    }
};
