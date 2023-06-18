import unittest
from api import get_salary_range_for_job 
import pandas as pd


df = pd.read_csv('data/ds_salaries.csv', index_col=0)
df = df.drop_duplicates()
df["salary"]=df["salary"]/1000.
df["salary_in_usd"] = df["salary_in_usd"]/1000.

class TestSalaryRange(unittest.TestCase):

    def test_no_filter(self):
        result = get_salary_range_for_job('Applied Machine Learning Scientist')
        expected_range = [31.875, 38.400,75.000, 423.00]
        self.assertEqual(result['salary_range'], expected_range)

    def test_filter_empty(self):
        result = get_salary_range_for_job('Applied Machine Learning Scientist', 
                                          company_location='FR')
        expected_range = []
        self.assertEqual(result['salary_range'], expected_range)

    def test_filter_non_empty(self):
        result = get_salary_range_for_job('Applied Machine Learning Scientist', 
                                                      company_location='US')
        expected_range = [38.400, 75.0, 423.00]
        self.assertEqual(result['salary_range'], expected_range)


if __name__ == '__main__':
    unittest.main()