defmodule LongestSubstringWithoutRepeatingCharactersTest do
  use ExUnit.Case

  import LongestSubstringWithoutRepeatingCharacters

  test "normal test" do
    assert 3 == lengthOfLongestSubstring("abcabcbb")
  end

  test "one char" do
    assert 1 == lengthOfLongestSubstring("a")
  end

  test "single char" do
    assert 1 == lengthOfLongestSubstring("aaaaaaaaaa")
  end
end
