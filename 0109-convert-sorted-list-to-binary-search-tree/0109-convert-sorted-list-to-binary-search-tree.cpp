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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    TreeNode* buildBST(vector<ListNode*>& indexedList, int left, int right){
        if(left == right)
            return nullptr;

        int mid = left + (right - left) / 2;
        TreeNode* root = new TreeNode(indexedList[mid]->val);
        root->left = buildBST(indexedList, left, mid);
        root->right = buildBST(indexedList, mid + 1, right);
        return root;
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        vector<ListNode*> indexedList;
        for(ListNode* node = head; node != nullptr; node = node->next)
            indexedList.push_back(node);

        return buildBST(indexedList, 0, indexedList.size());      
    }
};