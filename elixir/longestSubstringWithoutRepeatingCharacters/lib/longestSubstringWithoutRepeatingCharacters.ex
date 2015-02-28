defmodule LongestSubstringWithoutRepeatingCharacters do
    def lengthOfLongestSubstring(str) do
        {longest, length, _, _} = str |> String.to_char_list
        |> Enum.with_index
        |> Enum.reduce({0, 0, 0, %{}}, fn({c, index}, {longest, length, startIndex, occur}) ->
            lastIndex = Dict.get(occur, c)
            if lastIndex == nil do
                length = length + 1
            else
                occur = Enum.reduce(startIndex..lastIndex, occur, fn(i, acc) ->
                    Dict.delete(acc, String.at(str, i))
                end)
                if length > longest, do: longest = length
                startIndex = lastIndex + 1
                length = index - lastIndex
            end
            occur = Dict.put(occur, c, index)

            {longest, length, startIndex, occur}
        end)

        if length > longest, do: longest = length
        longest
    end
end
