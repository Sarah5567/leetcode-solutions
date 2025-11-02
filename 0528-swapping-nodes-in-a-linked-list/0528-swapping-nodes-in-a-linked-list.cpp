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
        ListNode* kthFromStart, * kthFromEnd = head;  
        int length = 0;

        for(ListNode* curNode = head; curNode; curNode = curNode->next){
            length++;
            if(length == k){
                kthFromStart = curNode;
            }
        }

        int requiredIndex = length - k + 1;
        for (int i = 1; i < requiredIndex; kthFromEnd = kthFromEnd->next, i++);
        
        int temp = kthFromStart->val;
        kthFromStart->val = kthFromEnd->val;
        kthFromEnd->val = temp;

        return head;
    }
};