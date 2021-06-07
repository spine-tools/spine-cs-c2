import pandas as pd
import sys 

test = sys.argv[0]
print(test)
##Read the data files
#File containing line capacities (and a lot of other stuff) from N490 model
lines_n490 = pd.read_excel(r'C:\Users\u0138303\Documents\Case Study C2\spatial-disaggregation\N490.xlsx',sheet_name='line').set_index('line_id')

#File containing line flows as calculated by SpineOpt
line_flows = pd.read_csv(r'C:\Users\u0138303\Documents\Spine_repos\spine-cs-c2\.spinetoolbox\items\line_flow_1\output\line_flow.csv',names=['Line','Time','Flow','Node','Direction','Scenario'])
line_flows =  line_flows[line_flows.Line != 'new_one']#Removal of unwanted lines
line_flows = line_flows[line_flows.Line != 'new_two']#Removal of unwanted lines

#Let's start by isolating the line capacities from the n490 output
line_capacities = pd.DataFrame(data = lines_n490.Cap)

#Then, let's isolate the to_node flows from the SpineOpt output, to avoid double counting
line_flows = line_flows[line_flows.Direction == 'to_node']
#And recast the line id's to integer type
line_flows['Line'] = line_flows['Line'].astype(int)

#We now reshape the dataframe so that we get a dataframe with the line id's as index levels
line_flows = pd.pivot_table(line_flows , values='Flow',columns='Time',index=['Line'], aggfunc=sum)

print('Line_flows have been pivoted')
#The capacities are then joined with the flow frame, so that the obtained flows can be easily compared to the estimated capacities. Note that only the 
#line-id's of the N490 frame are kept, since the spine-opt flows also include transformers, which we omit.
capacity_and_flows = line_capacities.join(line_flows,how = 'left')

#Then, some basic arithmetic operations are performed to rank the lines based on the accumulated usage rate, and the number of times that a line is congested.
usage_rate_frame = capacity_and_flows.iloc[:,1:].div(capacity_and_flows.Cap, axis=0)
acummulated_usage =  usage_rate_frame.abs().sum(axis=1)
nb_times_congested = usage_rate_frame[usage_rate_frame.abs()>1].count(axis=1)

rank_usage = acummulated_usage.rank(method = 'average', ascending = False)
rank_congested = nb_times_congested.rank(method = 'average',ascending = False)

#Finally, we sum the two rankings to obtain an estimate of the lines which are most eligible for investment
rank = rank_usage + rank_congested
rank = rank.sort_values()
print(rank)
rank.to_excel('Investment_candidates_SpineOpt_Nordic.xlsx')