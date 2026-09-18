import pandas as pd

#Using .query()
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.query('student_id == 101')[['name', 'age']]

#Using .loc — your current approach
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]