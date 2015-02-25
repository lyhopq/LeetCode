defmodule TwoSum do
	def towSum(nums, target) do
		ret = nums |> Enum.with_index
		|> Enum.reduce(%{:index1 => 0, :index2 => 0}, fn({num, index2}, acc) ->
			index1 = Dict.get(acc, target - num, nil)
			if index1 do
				acc |> Dict.put(:index1, index1)
					|> Dict.put(:index2, index2 + 1)
			else
				Dict.put(acc, num, index2 + 1)
			end	
		end
		)

		{Dict.get(ret, :index1), Dict.get(ret, :index2)}
	end
end
