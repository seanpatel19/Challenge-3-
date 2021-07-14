from pathlib import Path
import pandas as pd 


bitstamp_path = Path("./Resources/bitstamp.csv")

bitstamp_data = pd.read_csv(
    bitstamp_path, 
    index_col ="Date",
    infer_datetime_format = True,
    parse_dates = True)


import pandas as pd
import numpy as np

apple_df = pd.DataFrame({"AAPL": [72.27, np.nan, 74.39, np.nan, 75.94, 76.93,np.nan, 78.74, np.nan, 79.81, np.nan, 79.53, np.nan, 79.56, 79.49]})

apple_df