using Revise
using SpineOpt
using Gurobi
using JuMP
using Cbc

optimizer = optimizer_with_attributes(Gurobi.Optimizer, "OutputFlag" => 0, "MIPGap" => 1e-2)
m = run_spineopt(ARGS...; mip_solver=optimizer, lp_solver=optimizer)

#optimizer = optimizer_with_attributes(Cbc.Optimizer, "logLevel" => 0)
#m = run_spineopt(ARGS...)
