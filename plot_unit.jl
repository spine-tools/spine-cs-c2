using Gadfly
using CSV
using DataFrames
using Random
using Dates
import Cairo, Fontconfig

filepath = ARGS[1]
data = CSV.read(filepath, DataFrame)

nodes = unique(data[!, :node])

inds = randperm(length(nodes))[1:5]

@show somenodes = nodes[inds]

somenodes = [6433, 6126, 7758, 6736, 6726]

filter!(row -> row[:node] in somenodes, data)

p = plot(
	data,
	x=:time,
	y=:flow,
	color=:node,
	Geom.line,
	Guide.xticks(ticks=[DateTime(2021), DateTime(2026), DateTime(2031)]),
	Guide.xlabel("Year"),
	Guide.ylabel("Power flow (MWh)")
)
img = PNG("node_inj.png", 6inch, 4inch)
draw(img, p)
