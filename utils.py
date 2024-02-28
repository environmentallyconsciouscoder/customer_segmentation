import pandas as pd
import numpy as np
import sweetviz as sv

def open_csv_file(fileName: str) -> pd.DataFrame:
    data = pd.read_csv(fileName)
    return data

def create_csv_file(df: pd.DataFrame, fileName: str) -> pd.DataFrame:
    return df.to_csv(fileName)

def append_rows_dataframes(df_one: pd.DataFrame, df_two: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df_one, df_two])

def create_report(df):
    report = sv.analyze([df, 'sex_female'], target_feat='Survived')
    return report.show_html('Report.html')