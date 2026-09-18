import pandas as pd


#Using slicing
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:3]


#Using head()
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)