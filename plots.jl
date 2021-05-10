using Gadfly
using CSV
using DataFrames
using Random
using Dates
import Cairo, Fontconfig

filepath = ARGS[1]
data = CSV.read(filepath, DataFrame)

conns = unique(data[!, :connection])

inds = randperm(length(conns))[1:5]

@show someconns = conns[inds]

someconns = [6474, 2264, 2241, 458, 2372]

filter!(row -> row[:connection] in someconns, data)

p = plot(
	data,
	x=:time,
	y=:flow,
	color=:connection,
	Geom.line,
	Guide.xticks(ticks=[DateTime(2021), DateTime(2026), DateTime(2031)]),
	Guide.xlabel("Year"),
	Guide.ylabel("Power flow (MWh)")
)
img = PNG("conn_flow.png", 6inch, 4inch)
draw(img, p)
