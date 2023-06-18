# Salary Range API

This API provides the salary range for a specific job title, with optional filters for company location, experience level, and employment type. The salary range is returned as a sorted list under the 'salary_range' key. If a filter results in no matches, the API will return an empty list. If any of the parameters is invalid, the API will return a 400 error with an appropriate message.

You can find exploratory analysis in [analysis.ipynb](https://github.com/rolandina/simplon-projet-existant/blob/main/analysis.ipynb)

![](https://github.com/rolandina/simplon-projet-existant/blob/main/images/projet_donne_api.png)

## Endpoints

'GET /get_salary_range_for_job/'

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
pip install pandas fastapi uvicorn
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

For example for the request

```
http://0.0.0.0:8000/salary_range_for_job/?job_title=Data%20Scientist&company_location=US&experience_level=EN&employment_type=FjT
```

You will see the message
![](https://github.com/rolandina/simplon-projet-existant/blob/main/images/Projet_donne_Example_API_wrong_request.png)

## Contact information

If you have any questions you can contact me by email:
ms.nina.smirnova@gmail.com
