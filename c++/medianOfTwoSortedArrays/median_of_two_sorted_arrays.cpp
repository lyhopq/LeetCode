#include "median_of_two_sorted_arrays.h"

int middle(int low, int high)
{
	return low + (high - low)/2;
}

int binarySeach(int A[], int low, int high, int key)
{
	while(low <= high)
	{
		int mid = middle(low, high);
		if(key == A[mid]) return mid;
		if(key > A[mid])
		{
			low = mid + 1;
		}
		else
		{
			high = mid - 1;
		}

	}

	return low;
}

double findMedianSortedArrayHelper(int A[], int m, int B[], int n, 
	int lowA, int highA, int lowB, int highB)
{
	int mid = middle(lowA, highA);
	int pos = binarySeach(B, lowB, highB, A[mid]);
	int num = mid + pos;

	if(num == (m+n)/2)
	{
		int first = 0;
		if((m+n)%2 == 1) return double(A[mid]);
		if(mid > 0 && pos > 0) first = A[mid-1] > B[pos-1] ? A[mid-1] : B[pos-1];
		else if(pos > 0) first = B[pos-1];
		else if(mid > 0) first = A[mid-1];

		return (first + A[mid])/2.0;
	}

	if(num < (m+n)/2)
	{
		lowA = mid + 1;
		lowB = pos;
	}
	else if(num > (m+n)/2)
	{
		highA = mid - 1;
		highB = pos - 1;
	}

    if(highA - lowA > highB - lowB)
    {
    	return findMedianSortedArrayHelper(A, m, B, n, lowA, highA, lowB, highB);
    }
    return findMedianSortedArrayHelper(B, n, A, m, lowB, highB, lowA, highA);
}

double findMedianSortedArrays(int A[], int m, int B[], int n)
{
    if(m == 0 && n == 0) return 0.0;
    if(m == 0) return n%2==1 ? float(B[n/2]) : (B[n/2-1] + B[n/2])/2.0;
    if(n == 0) return m%2==1 ? float(A[m/2]) : (A[m/2-1] + A[m/2])/2.0;

    if(m >= n)
    {
        return findMedianSortedArrayHelper(A, m, B, n, 0, m - 1, 0, n - 1);
    }
    return findMedianSortedArrayHelper(B, n, A, m, 0, n - 1, 0, m - 1);
}
