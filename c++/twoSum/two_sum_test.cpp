#include <gtest/gtest.h>

#include "two_sum.h"

TEST(twoSumTest, two_sun_exist)
{
    VECTOR result{1, 2};
    VECTOR in{2, 7, 11, 15};
    ASSERT_EQ(result, twoSum(in, 9));
}

TEST(twoSumTest, two_sun_not_exist)
{
    VECTOR result{0, 0};
    VECTOR in{2, 5, 11, 15};
    ASSERT_EQ(result, twoSum(in, 9));
}

int main(int argc, char *argv[])
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

