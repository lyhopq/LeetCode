defmodule MedianOfTwoSortedArraysTest do
  use ExUnit.Case
  import MedianOfTwoSortedArrays

  test "two empty arrays" do
    assert 0.0 == findMedianSortedArrays([], [])
  end

  test "first array is empty" do
    assert 2.0 == findMedianSortedArrays([], [1,2,3])
    assert 2.5 == findMedianSortedArrays([], [1,2,3,4])
  end

  test "second array is empty" do
    assert 2.0 == findMedianSortedArrays([1,2,3], [])
    assert 2.5 == findMedianSortedArrays([1,2,3,4], [])
  end

  test "normal arrays" do
    assert 18.0 == findMedianSortedArrays([5,7,11,17,18,21], [13,16,19,22,27,30,31])
  end
end
