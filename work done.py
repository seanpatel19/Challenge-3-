from pathlib import Path
import pandas as pd 


bitstamp_path = Path("./Resources/bitstamp.csv")

bitstamp_data = pd.read_csv(
    bitstamp_path, 
    index_col ="Date",
    infer_datetime_format = True,
    parse_dates = True)
