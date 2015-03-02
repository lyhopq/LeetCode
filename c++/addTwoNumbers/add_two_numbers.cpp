#include <iostream>
#include "add_two_numbers.h"

using namespace std;

ListNode::ListNode(int x) : val(x), next(nullptr) {}

string ListNode::toString()
{
	string result;
	ListNode * li = this;
	while(li != nullptr)
	{
		result += li->val;
		li = li->next;
	}

	return result;
}

int getValueAndMoveNext(ListNode* &li)
{
	int x = 0;
	if(li != nullptr)
	{
		x = li->val;
		li = li->next;
	}

	return x;
}

ListNode *addTwoNumbers(ListNode* l1, ListNode* l2)
{
	int d1 = 0, d2 = 0, carry = 0, sum = 0;
	ListNode *result = nullptr;
	ListNode **p = &result;

	while(l1 != nullptr || l2 != nullptr)
	{
		d1 = getValueAndMoveNext(l1);
		d2 = getValueAndMoveNext(l2);

		sum = carry + d1 + d2;

		ListNode *node = new ListNode(sum%10);
		*p = node;
		p = &node->next;

		carry = sum/10;
	}

	if(carry > 0)
	{
		ListNode *node = new ListNode(carry);
		*p = node;
	}

	return result;
}
