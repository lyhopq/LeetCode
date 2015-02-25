defmodule TwoSumTest do
  use ExUnit.Case

  test "tow sum exits" do
    assert TwoSum.towSum([2, 7, 11, 15], 9) == {1, 2}
    assert TwoSum.towSum([2, 7, 11, 15], 22) == {2, 4}
  end

  test "tow sum not exits" do
    assert TwoSum.towSum([2, 7, 11, 14], 22) == {0, 0}
  end

end
