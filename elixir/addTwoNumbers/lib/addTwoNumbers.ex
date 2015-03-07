defmodule ListNode do
    defstruct val: 0, next: nil 

    def addTwoNumbers(l1, l2) do
      addTwoNumbersHelper(l1, l2, 0, [])
    end
    defp addTwoNumbersHelper(nil, nil, carry, li) do
      if carry != 0 do
        createNodeList([carry | li] |> Enum.reverse)
      else
        createNodeList(li |> Enum.reverse)
      end
    end
    defp addTwoNumbersHelper(nil, l2, carry, li) do
      addTwoNumbersHelper(%ListNode{}, l2, carry, li)
    end
    defp addTwoNumbersHelper(l1, nil, carry, li) do
      addTwoNumbersHelper(l1, %ListNode{}, carry, li)
    end
    defp addTwoNumbersHelper(%ListNode{val: d1, next: l1}, %ListNode{val: d2, next: l2}, carry, li) do
      sum = d1 + d2 + carry
      addTwoNumbersHelper(l1, l2, div(sum, 10), [rem(sum, 10) | li])
    end

    def createNodeList(li) do
      createNodeListHelper(li |> Enum.reverse, nil)
    end

    defp createNodeListHelper([], result), do: result
    defp createNodeListHelper([head | tail], result) do
      createNodeListHelper(tail, %ListNode{val: head, next: result})
    end

    def toString(%ListNode{val: val, next: node}, s \\ "") do
      s = s <> to_string(val)
      if node == nil do
        s
      else
        toString(node, s)
      end
    end
end
