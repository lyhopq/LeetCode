defmodule AddTwoNumbersTest do
  use ExUnit.Case
  import ListNode

  test "equal_numbers" do
    l1 = createNodeList([2,4,3])
    l2 = createNodeList([5,6,4])
    assert addTwoNumbers(l1, l2) == createNodeList([7,0,8])
  end

  test "not_equal_numbers" do
    l1 = createNodeList([2])
    l2 = createNodeList([5,6,4])
    assert addTwoNumbers(l1, l2) == createNodeList([7,6,4])
  end

  test "carry_muti_times" do
    l1 = createNodeList([9,9,9])
    l2 = createNodeList([2])
    assert addTwoNumbers(l1, l2) == createNodeList([1,0,0,1])
  end
end
