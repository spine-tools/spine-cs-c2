from nordic490 import N490
m = N490(year=2018)
m.branch_params()
load, gen, link = m.get_measurements('20180120:18')  # download data for a certain hour
m.distribute_power(load, gen, link)  # distribute on buses and gens (simple method)
m.dcpf()
m.save_xlsx('N490.xlsx')  # save to excel