import pandas as pd
import sys 

line_flow_path, N490_path = sys.argv[1], sys.argv[2]
## Read the data files
# File containing line capacities (and a lot of other stuff) from N490 model
lines_n490 = pd.read_excel(N490_path,sheet_name='line').set_index('line_id')

# File containing line flows as calculated by SpineOpt
invested_line_ids = pd.read_csv(line_flow_path)
invested_line_ids = [int(x.replace("_new", "")) for x in invested_line_ids["line_id"]]

# Finally we pick the first 10 lines into a new DF for importing into a Spine DB
invested_lines = lines_n490.loc[invested_line_ids]
invested_lines = invested_lines.rename(lambda x: str(x) + "_invested", axis='index')

invested_lines.to_excel('Invested_lines_Nordic.xlsx')