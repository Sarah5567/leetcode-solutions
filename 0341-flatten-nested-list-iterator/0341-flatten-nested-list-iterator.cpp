class NestedIterator {
private:
    stack<pair<const vector<NestedInteger>*, int>> st;

    void moveToNextInteger() {
        while (!st.empty()) {
            auto &[lst, idx] = st.top();

            if (idx >= (int)lst->size()) {
                st.pop();
                if (!st.empty()) st.top().second++;
                continue;
            }

            if ((*lst)[idx].isInteger()) return;

            const vector<NestedInteger> &sub = (*lst)[idx].getList();
            st.push({&sub, 0});
        }
    }

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        st.push({&nestedList, 0});
        moveToNextInteger();
    }

    int next() {
        int val = (*st.top().first)[st.top().second].getInteger();
        st.top().second++;
        moveToNextInteger();
        return val;
    }

    bool hasNext() {
        moveToNextInteger();
        return !st.empty();
    }
};
