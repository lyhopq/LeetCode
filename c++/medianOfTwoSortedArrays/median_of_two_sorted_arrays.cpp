#include <map>
#include <algorithm>

#include "two_sum.h"

typedef std::map<int, int> MAP;

VECTOR twoSum(VECTOR &numbers, int target) 
{
	VECTOR result{0, 0};
	auto index = 0;
	MAP indexMap;
	for(auto num : numbers)
	{
		auto iter = indexMap.find(target - num); 
		if(iter != indexMap.end())
		{
			result[0] = iter->second + 1;
			result[1] = index + 1;

			return result;
		}

		indexMap[num] = index++;
	}

	return result;
}
