/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;
        for (auto node : lists)
            if (node)
                minHeap.push(node);

        ListNode* sortedList = nullptr;
        ListNode* tail = nullptr;

        while (!minHeap.empty()) {
            ListNode* node = minHeap.top();
            minHeap.pop();

            if (!sortedList) {
                sortedList = tail = node;
            } else {
                tail->next = node;
                tail = tail->next;
            }

            if (node->next)
                minHeap.push(node->next);
        }

        return sortedList;

    }
};