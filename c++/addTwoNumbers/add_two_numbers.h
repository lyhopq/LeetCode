#include <string>

struct ListNode
{
    int val;
    ListNode *next;

    ListNode(int x);

    std::string toString();
};

template<typename... Tlist>  
ListNode* CreatListNode(Tlist... li) 
{  
    ListNode *result = nullptr;
    ListNode **p = &result;
    creatListNode(p, li...);
    return result;  
}

template <typename ... Tlist>
void creatListNode(ListNode** p)
{
}

template<typename T, typename... Tlist>  
void creatListNode(ListNode** p, T head, Tlist... tail) 
{  
    ListNode* node = new ListNode(head);
    *p = node;
    p = &node->next;

    creatListNode(p, tail...);
} 

void Print(ListNode *li);
ListNode *addTwoNumbers(ListNode *l1, ListNode *l2);
