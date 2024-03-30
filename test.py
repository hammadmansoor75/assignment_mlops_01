import pandas as pd
import os


def test_csv_file_exists():
    assert os.path.isfile('./Dataset/student.csv'), "CSV file does not exist."


def test_read_csv():
    df = pd.read_csv('./Dataset/student.csv')
    assert not df.empty, "CSV file is empty."
    assert 'Student_Age' in df.columns, "'Student_Age' column not in CSV."

# Adding a newline at the end of the file
