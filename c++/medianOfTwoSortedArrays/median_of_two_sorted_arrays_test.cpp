#include <gtest/gtest.h>

#include "median_of_two_sorted_arrays.h"

TEST(median_of_two_sorted_arrays, odd_length)
{
	int A[] = {5,7,11,17,18,21};
	int B[] = {13,16,19,22,27,30,31};
	int m = sizeof(A)/sizeof(A[0]);
	int n = sizeof(B)/sizeof(B[0]);

    ASSERT_EQ(18.0, findMedianSortedArrays(A, m, B, n));
}

TEST(median_of_two_sorted_arrays, even_length)
{
	int A[] = {5,7,11,17,18,21};
	int B[] = {13,16,19,22,27,30};
	int m = sizeof(A)/sizeof(A[0]);
	int n = sizeof(B)/sizeof(B[0]);

    ASSERT_EQ(17.5, findMedianSortedArrays(A, m, B, n));
}

int main(int argc, char *argv[])
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

