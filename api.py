from fastapi import FastAPI, HTTPException
from typing import Optional, List
import pandas as pd
from enum import Enum


class ExperienceLevel(str, Enum):
    EN = "EN"
    MI = "MI"
    SE = "SE"
    EX = "EX"

class EmploymentType(str, Enum):
    PT = "PT"
    FL = "FL"
    FT = "FT"
    CT = "CT"


app = FastAPI(title="Get Salary Range for the Data Science job")


df = pd.read_csv('data/ds_salaries.csv', index_col=0)
df = df.drop_duplicates()
df["salary"]=df["salary"]/1000
df["salary_in_usd"] = df["salary_in_usd"]/1000 


@app.get("/")
def read_root():
    return {"Hello": "Welcome to the Salary Range API! Use /get_salary_range_for_job endpoint to get the salary range for a specific job."}



def get_salary_range_for_job(job_title: str, company_location: Optional[str] = None, 
                             experience_level: Optional[str] = None, employment_type: Optional[str] = None):
    df_filtered = df[df['job_title'] == job_title]
    
    if company_location is not None:
        df_filtered = df_filtered[df_filtered['company_location'] == company_location]
        if df_filtered.empty:
            return {"salary_range": []}
            
    if experience_level is not None:
        df_filtered = df_filtered[df_filtered['experience_level'] == experience_level]
        if df_filtered.empty:
            return {"salary_range": []}
            
    if employment_type is not None:
        df_filtered = df_filtered[df_filtered['employment_type'] == employment_type]
        if df_filtered.empty:
            return {"salary_range": []}
    
    salary_range = df_filtered['salary_in_usd'].tolist()
    salary_range.sort()
    
    return {"salary_range": salary_range}




@app.get("/salary_range_for_job/")
async def salary_range_for_job(job_title: str, company_location: Optional[str] = None, 
                                     experience_level: ExperienceLevel = None, 
                                     employment_type: EmploymentType = None):
 
    if job_title not in df['job_title'].unique():
        raise HTTPException(status_code=400, detail=f"Invalid job_title. Please choose from {df['job_title'].unique().tolist()}")

    if company_location is not None and company_location not in df['company_location'].unique():
        raise HTTPException(status_code=400, detail=f"Invalid company_location. Please choose from {df['company_location'].unique().tolist()}")

    # if experience_level is not None and experience_level not in df['experience_level'].values:
    #     raise HTTPException(status_code=400, detail="Experience level not found")
        
    # if employment_type is not None and employment_type not in df['employment_type'].values:
    #     raise HTTPException(status_code=400, detail="Employment type not found")
    
    return get_salary_range_for_job(job_title, company_location, experience_level, employment_type)





# @app.get(
#     "/get_salary_range_for_job/",
#     summary="Get salary range for a specific job",
#     description="This endpoint returns the range (min, mean, max) of salary in USD for a specific job. You can also filter the results based on company location, experience level, and employment type. If the company location is not indicated, it returns the salary range for all locations. If the experience level or employment type is indicated, it filters the salary range accordingly. The salary range is sorted in ascending order.",
#     response_description="The minimum and maximum salary in USD for the specified job, optionally filtered by company location, experience level, and employment type.",
#     responses={
#         200: {
#             "description": "Salary range retrieved successfully",
#             "content": {
#                 "application/json": {
#                     "example": [50000.0, 100000.0, 150000.0]
#                 }
#             }
#         },
#         400: {"description": "Invalid input"}
#     }
# )
# async def get_salary_range_for_job(job_title: str,
#                                    company_location: str = None,
#                                    experience_level: ExperienceLevel = None,
#                                    employment_type: EmploymentType = None):
    
#     if job_title not in df['job_title'].unique():
#         raise HTTPException(status_code=400, detail=f"Invalid job_title. Please choose from {df['job_title'].unique().tolist()}")

#     if company_location is not None and company_location not in df['company_location'].unique():
#         raise HTTPException(status_code=400, detail=f"Invalid company_location. Please choose from {df['company_location'].unique().tolist()}")

#     # if experience_level is not None and experience_level not in df['experience_level'].unique():
#     #     raise HTTPException(status_code=400, detail=f"Invalid experience_level. Please choose from {df['experience_level'].unique().tolist()}")

#     # if employment_type is not None and employment_type not in df['employment_type'].unique():
#     #     raise HTTPException(status_code=400, detail=f"Invalid employment_type. Please choose from {df['employment_type'].unique().tolist()}")

#     response = dict()
#     # Filter based on the job_title
#     df_filtered = df[df['job_title'] == job_title]

#     # If DataFrame is empty after filtering, return a message
#     if df_filtered.empty:
#         response["message"] = "No jobs found with the given job title."
#         return response

#     # If experience_type is given, apply the filter
#     if experience_level:
#         df_filtered = df_filtered[df_filtered['experience_level'] == experience_level]

#         # If DataFrame is empty after filtering, return a message
#         if df_filtered.empty:
#             response["message"] = "No jobs found with the given job title and experience type."
#             return response

#     # If company_location is given, apply the filter
#     if company_location:
#         df_filtered = df_filtered[df_filtered['company_location'] == company_location]

#         # If DataFrame is empty after filtering, return a message
#         if df_filtered.empty:
#             response["message"] = "No jobs found for the given job title with indicated company location."
#             return response

#     # If employment_type is given, apply the filter
#     if employment_type:
#         df_filtered = df_filtered[df_filtered['employment_type'] == employment_type]

#         # If DataFrame is empty after filtering, return a message
#         if df_filtered.empty:
#             response["message"] = "No jobs found with the given job title, experience type, company location, and employment type."
#             return response

#     # After applying all filters, compute the salary range
#     salary_range = df_filtered['salary_in_usd']

#     response["salary_range"] = salary_range.values
#     return response


  


import uvicorn
if __name__=='__main__':
    uvicorn.run("api:app", host="0.0.0.0", reload=False)