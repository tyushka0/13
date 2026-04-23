'превращение файла в DataFrame'
import pandas as pd

def load_data(path: str = "data/workouts.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df