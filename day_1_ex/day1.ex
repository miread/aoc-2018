# defmodule Calibrate do
#   def import(filename) do
#     File.stream!(filename)
#     |> Stream.map(&String.replace(&1, "\n", ""))
#     |> Stream.map(&String.to_integer(&1))
#     |> Enum.reduce(fn(x, acc) -> x + acc end)
#   end
# end

defmodule Calibrate do
  def import_input(start_map \\ [0, %{}]) do
    input = File.stream!("input.txt")
    |> Stream.map(&String.replace(&1, "\n", ""))
    |> Stream.map(&String.to_integer(&1))
    Enum.reduce(input, start_map, fn(x, acc) ->
      proc(acc, x)
    end)
    |> import_input()
  end

  def proc(acc, input) do
    [oldnum, map] = acc
    newnum = oldnum + input
    cond do
      Map.has_key?(map, newnum) -> IO.puts("#{newnum} appeared twice!")
      true -> nil
    end
    map = Map.put(map, newnum, "true")
    [newnum, map]
  end
end
