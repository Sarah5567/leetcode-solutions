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
    int findNodes(ListNode* curNode, pair<ListNode*, ListNode*>& requestedNodes, int& k, int index){
        if(!curNode)
            return 1;

        if(index == k)
            requestedNodes.first = curNode;
        
        int reversedIndex = findNodes(curNode->next, requestedNodes, k, index + 1);
        if(reversedIndex == k)
            requestedNodes.second = curNode;

        return reversedIndex + 1;
    }
public:
    ListNode* swapNodes(ListNode* head, int k) {
        pair<ListNode*, ListNode*> nodes;
        findNodes(head, nodes, k, 1);
        
        int temp = nodes.first->val;
        nodes.first->val = nodes.second->val;
        nodes.second->val = temp;

        return head;
    }
};