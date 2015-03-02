#include <gtest/gtest.h>

#include "add_two_numbers.h"

TEST(add_two_numbers, equal_numbers)
{
    ListNode* l1 = CreatListNode(2,4,3);
    ListNode* l2 = CreatListNode(5,6,4);
    ListNode* result = CreatListNode(7,0,8);
    ASSERT_EQ(result->toString(), addTwoNumbers(l1, l2)->toString());
}

TEST(add_two_numbers, not_equal_numbers)
{
    ListNode* l1 = CreatListNode(2);
    ListNode* l2 = CreatListNode(5,6,4);
    ListNode* result = CreatListNode(7,6,4);
    ASSERT_EQ(result->toString(), addTwoNumbers(l1, l2)->toString());
}

TEST(add_two_numbers, carry_muti_times)
{
    ListNode* l1 = CreatListNode(9,9,9);
    ListNode* l2 = CreatListNode(2);
    ListNode* result = CreatListNode(1,0,0,1);
    ASSERT_EQ(result->toString(), addTwoNumbers(l1, l2)->toString());
}

int main(int argc, char *argv[])
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

