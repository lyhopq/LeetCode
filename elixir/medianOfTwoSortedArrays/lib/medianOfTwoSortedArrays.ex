defmodule MedianOfTwoSortedArrays do
	def findMedianSortedArrays([], []), do: 0.0
	def findMedianSortedArrays([], b), do: findMedianSortedArray(b)
	def findMedianSortedArrays(a, []), do: findMedianSortedArray(a)
	def findMedianSortedArrays(a, b) do
    m = length(a)
    n = length(b)

    if m >= n do
    	findMedianSortedArrayHelper(a, b, 0, m - 1, 0, n - 1)
    else
    	findMedianSortedArrayHelper(b, a, 0, n - 1, 0, m - 1)
    end
	end

	defp middle(low, high), do: low + div(high - low, 2)
	defp findMedianSortedArray(a) do
		len = length(a)
	  mid = middle(0, len)
	  if rem(len, 2) == 1 do
	  	Enum.at(a, mid)
	  else
	  	(Enum.at(a, mid - 1) + Enum.at(a, mid))/2
	  end
	end

	defp binarySeach(_, low, high, _) when low > high, do: low
	defp binarySeach(a, low, high, key) do
		mid = middle(low, high)	
		cond do
			key > Enum.at(a, mid) -> binarySeach(a, mid + 1, high, key)
			key < Enum.at(a, mid) -> binarySeach(a, low, mid - 1, key)
			true -> mid
		end
	end
			
	defp findMedianSortedArrayHelper(a, b, lowa, higha, lowb, highb) do
		mid = middle(lowa, higha)
		pos = binarySeach(b, lowb, highb, Enum.at(a, mid))
		num = mid + pos
		m = length(a)
		n = length(b)
		cond do
			num == div(m+n, 2) ->
				if rem(m+n, 2) == 1 do
					Enum.at(a, mid)
				else
					first = cond do
						mid > 0 and pos > 0 ->
							if Enum.at(a, mid - 1) > Enum.at(b, pos - 1) do
								Enum.at(a, mid - 1)
							else
								Enum.at(b, pos - 1)
							end
						pos > 0 ->
							Enum.at(b, pos - 1)
						mid > 0 ->
							Enum.at(a, mid - 1)
					end
					(first + Enum.at(a, mid))/2
				end
			num < div(m+n, 2) ->
				lowa = mid + 1
				lowb = pos
				if higha - lowa > highb - lowb do
					findMedianSortedArrayHelper(a, b, lowa, higha, lowb, highb)
				else
					findMedianSortedArrayHelper(b, a, lowb, highb, lowa, higha)
				end
			true ->
				higha = mid - 1
				highb = pos - 1
				if higha - lowa > highb - lowb do
					findMedianSortedArrayHelper(a, b, lowa, higha, lowb, highb)
				else
					findMedianSortedArrayHelper(b, a, lowb, highb, lowa, higha)
				end
		end
	end
end
