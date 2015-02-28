#include <map>
#include <algorithm>

#include "longest_substring_without_repeating_characters.h"

int lengthOfLongestSubstring(string str)
{
    map<char, int> occur;
    auto length = 0;
    auto longest = 0;
    auto startIndex = 0;
    for(auto index = 0; index < str.length(); index++)
    {
        auto c = str[index];
        auto iter = occur.find(c); 
        if(iter == occur.end())
        {
            occur[c] = index;
            length += 1;
        }
        else
        {
            auto lastIndex = iter->second;
            for(auto i = startIndex; i < lastIndex; i++)
            {
                auto deleteIter = occur.find(str[i]);
                occur.erase(deleteIter);
            }
            if(length > longest) longest = length;
            startIndex = lastIndex + 1;
            length = index - lastIndex;
            occur[c] = index;
        }
    }

    if(length > longest) longest = length;

    return longest;
}
