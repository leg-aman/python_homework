# task5_extended_df.py

import pandas as pd

class FancyDataFrame(pd.DataFrame):
    @property
    def _constructor(self):
        return FancyDataFrame

    @classmethod
    def load_csv(cls, path, **options):
        base_df = pd.read_csv(path, **options)
        return cls(base_df)

    def show_rows_in_parts(self):
        num_rows = len(self)
        if num_rows == 0:
            print("⚠️  Oops, this DataFrame is empty.")
            return

        rows_per_chunk = 5  # Changed from 10 to 5 for smaller batches
        chunk_start = 0

        while chunk_start < num_rows:
            chunk_end = chunk_start + rows_per_chunk
            if chunk_end > num_rows:
                chunk_end = num_rows

            print("\nShowing rows {} to {}:".format(chunk_start + 1, chunk_end))
            print(self.iloc[chunk_start:chunk_end])
            chunk_start += rows_per_chunk


# Example usage
fdf = FancyDataFrame.load_csv("../csv/products.csv")
fdf.show_rows_in_parts()
