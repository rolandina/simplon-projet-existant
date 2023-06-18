# Data Science jobs salary API

You can find exploratory analysis in [analysis.ipynb](https://github.com/rolandina/simplon-projet-existant/blob/main/analysis.ipynb)

![](https://github.com/rolandina/simplon-projet-existant/blob/main/images/projet_donne_api.png)

## Endpoint /predict_salary

This endpoint uses a trained Gradient boost model to make a prediction of salary based on job and company details. The function predict_salary takes in several parameters as inputs:

- **experience_level**: Level of experience required for the job (Enumeration of all experience levels in dataset).
- **employment_type**: Type of employment (Enumeration of all employment types in dataset).
- **job_title**: Title of the job (Enumeration of all job titles in dataset).
- **employee_residence**: Residence of the employee (Enumeration of all possible residences in dataset).
- **remote_ratio**: Remote work ratio for the job (Enumeration of all possible remote ratios in dataset).
- **company_location**: Location of the company (Enumeration of all possible company locations in dataset).
- **company_size**: Size of the company (Enumeration of all possible company sizes in your dataset).
- **work_year**: Year of work. The year should be between 2020 and 2022.

The endpoint creates a DataFrame from the input data and encodes it using a established encoding scheme. It then makes a prediction using a trained model and returns the predicted salary.

### Example of usage

```bash
curl -X GET "http://0.0.0.0:8000/predict_salary?experience_level=EN&employment_type=FT&job_title=Data%20Scientist&employee_residence=FR&remote_ratio=0&company_location=FR&company_size=L&work_year=2021"
```

### Example of response

Returns a JSON response with the predicted salary, e.g.

```json
{
  "result": 95.0
}
```

## Endpoint /get_salary_range_for_job/

This endpoint provides the salary range for a specific job title, with optional filters for company location, experience level, and employment type. The salary range is returned as a sorted list under the 'salary_range' key. If a filter results in no matches, the API will return an empty list. If any of the parameters is invalid, the API will return a 400 error with an appropriate message.

Fetches the salary range for a specific job title.

### Parameters:

- **job_title** (string): The job title to fetch the salary range for (required).
- **company_location** (string): An optional filter to get the salary range for a specific company location.
- **experience_level** (string): An optional filter to get the salary range for a specific experience level.
- **employment_type** (string): An optional filter to get the salary range for a specific employment type.

### Example Usage

```bash
curl -X GET "http://0.0.0.0:8000/salary_range_for_job/?job_title=Data%20Scientist&company_location=US&experience_level=EN&employment_type=FT"
```

### Example Response

```json
{
  "salary_range": [58, 80, 90, 100, 100, 105]
}
```

## Setup and Run

1. Install FastAPI and Uvicorn:

```bash
pip install pandas fastapi uvicorn typing
```

2. Run the server by running the [api.py](https://github.com/rolandina/simplon-projet-existant/blob/main/api.py) file:

```bash
python3 api.py
```

## Running Unit Test

For this project, I have a set of unit tests implemented in the [test_salary_range_for_job.py](https://github.com/rolandina/simplon-projet-existant/blob/main/test_salary_range_for_job.py) file.

To run these unit tests, follow these steps:

1. Ensure you have the unittest package installed. You can install it using pip:

```
pip install unittest
```

2. Navigate to the root directory of the project containing the test_salary_range_for_job.py and run the unit tests using the following command:

```
python -m unittest test_salary_range_for_job.py
```

You should see something like this:
![](<[images/Screenshot%20from%202023-06-18%2012-04-58.png](https://github.com/rolandina/simplon-projet-existant/blob/main/images/Screenshot%20from%202023-06-18%2012-04-58.png)>)

## Example of wrong request

This API has a protection against the wrong request, it was accomplished by creating a Enum class for each parameter.

For example for the request get /salary_range for the job

```
http://0.0.0.0:8000/salary_range_for_job/?job_title=Data%20Scientist&company_location=US&experience_level=EN&employment_type=FjT
```

You will see the message
![](https://github.com/rolandina/simplon-projet-existant/blob/main/images/Projet_donne_Example_API_wrong_request.png)

## Contact information

If you have any questions you can contact me by email:
ms.nina.smirnova@gmail.com
