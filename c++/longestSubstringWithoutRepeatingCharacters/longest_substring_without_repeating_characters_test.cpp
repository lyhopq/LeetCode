#include <gtest/gtest.h>

#include "longest_substring_without_repeating_characters.h"

TEST(lengthOfLongestSubstring, normal_test)
{
    ASSERT_EQ(3, lengthOfLongestSubstring("abcabcbb"));
}

TEST(lengthOfLongestSubstring, one_char)
{
    ASSERT_EQ(1, lengthOfLongestSubstring("a"));
}

TEST(lengthOfLongestSubstring, single_char)
{
    ASSERT_EQ(1, lengthOfLongestSubstring("aaaaaaaa"));
}

int main(int argc, char *argv[])
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

