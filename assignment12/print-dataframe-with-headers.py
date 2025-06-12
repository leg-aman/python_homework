
# Task 5: Extending a Class

import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)
    
    def print_with_headers(self):
        all_rows = len(self)
        if all_rows == 0:
            print("⚠️ oops! DataFrame is empty.")
            return
        
        for row_beg in range(0, all_rows, 10):
            row_last = min(row_beg +10, all_rows)
            res = self.iloc[row_beg:row_last]
            print(f"Rows {row_beg + 1} to {row_last}:")
            print(res)


dfp = DFPlus.from_csv("../csv/products.csv")
dfp.print_with_headers()
