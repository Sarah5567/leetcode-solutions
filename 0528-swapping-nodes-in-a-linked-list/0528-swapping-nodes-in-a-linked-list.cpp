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
    ListNode* swapNodes(ListNode* head, int k) {
        pair<ListNode*, ListNode*> nodes;
        int length = 0;
        ListNode* curNode;

        for(curNode = head; curNode; curNode = curNode->next){
            length++;
            if(length == k){
                nodes.first = curNode;
            }
        }
        
        nodes.second = head;
        for (int i = 1; i < length - k + 1; nodes.second = nodes.second->next, i++);
        
        int temp = nodes.first->val;
        nodes.first->val = nodes.second->val;
        nodes.second->val = temp;

        return head;
    }
};