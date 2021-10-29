using Revise
using SpineOpt
# sing Gurobi
using JuMP
using Gurobi

# optimizer = optimizer_with_attributes(Gurobi.Optimizer, "OutputFlag" => 0, "MIPGap" => 1e-2)
# m = run_spineopt(ARGS...; mip_solver=optimizer, lp_solver=optimizer)

optimizer = optimizer_with_attributes(Gurobi.Optimizer, "logLevel" => 3)
m = run_spineopt(ARGS...)
