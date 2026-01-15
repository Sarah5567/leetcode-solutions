class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        for(ListNode** cur = &head; *cur && (*cur)->next; cur = &((*cur)->next->next)){
            ListNode* first = (*cur), *second = (*cur)->next;
            *cur = second;
            first->next = second->next;
            second->next=first;
        }
        return head;
    }
};