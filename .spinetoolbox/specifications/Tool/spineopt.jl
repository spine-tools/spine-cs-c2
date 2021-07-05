using Revise
using SpineOpt
using Gurobi
using JuMP
using Cbc

optimizer = optimizer_with_attributes(Gurobi.Optimizer, "OutputFlag" => 0, "MIPGap" => 1e-2)
db_url_in = "sqlite:///C:\\Users\\u0138303\\Documents\\Spine_repos\\spine-cs-c2\\.spinetoolbox\\items\\input\\input.sqlite"
db_url_out = "sqlite:///C:\\Users\\u0138303\\Documents\\Spine_repos\\spine-cs-c2\\.spinetoolbox\\items\\output\\output.sqlite"

m = run_spineopt(db_url_in,db_url_out, mip_solver=optimizer, lp_solver=optimizer)
# m = run_spineopt(ARGS...)

# optimizer = optimizer_with_attributes(Cbc.Optimizer, "logLevel" => 0)
# m = run_spineopt(ARGS...)
