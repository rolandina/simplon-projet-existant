from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
import pandas as pd
from enum import Enum
from joblib import load

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

class RemoteRatio(str, Enum):
    no_remote = 0
    half_remote = 50
    full_remote = 100

class EmployeeResidence(str, Enum):
    AE = "AE"
    AR = "AR"
    AT = "AT"
    AU = "AU"
    BE = "BE"
    BG = "BG"
    BO = "BO"
    BR = "BR"
    CA = "CA"
    CH = "CH"
    CL = "CL"
    CN = "CN"
    CO = "CO"
    CZ = "CZ"
    DE = "DE"
    DK = "DK"
    DZ = "DZ"
    EE = "EE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    GR = "GR"
    HK = "HK"
    HN = "HN"
    HR = "HR"
    HU = "HU"
    IE = "IE"
    IN = "IN"
    IQ = "IQ"
    IR = "IR"
    IT = "IT"
    JE = "JE"
    JP = "JP"
    KE = "KE"
    LU = "LU"
    MD = "MD"
    MT = "MT"
    MX = "MX"
    MY = "MY"
    NG = "NG"
    NL = "NL"
    NZ = "NZ"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PR = "PR"
    PT = "PT"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    SG = "SG"
    SI = "SI"
    TN = "TN"
    TR = "TR"
    UA = "UA"
    US = "US"
    VN = "VN"


class CompanyLocation(str, Enum):
    AE = "AE"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CH = "CH"
    CL = "CL"
    CN = "CN"
    CO = "CO"
    CZ = "CZ"
    DE = "DE"
    DK = "DK"
    DZ = "DZ"
    EE = "EE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    GR = "GR"
    HN = "HN"
    HR = "HR"
    HU = "HU"
    IE = "IE"
    IL = "IL"
    IN = "IN"
    IQ = "IQ"
    IR = "IR"
    IT = "IT"
    JP = "JP"
    KE = "KE"
    LU = "LU"
    MD = "MD"
    MT = "MT"
    MX = "MX"
    MY = "MY"
    NG = "NG"
    NL = "NL"
    NZ = "NZ"
    PK = "PK"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    RU = "RU"
    SG = "SG"
    SI = "SI"
    TR = "TR"
    UA = "UA"
    US = "US"
    VN = "VN"

class CompanySize(str, Enum):
    S = "S"
    M = "M"
    L = "L"

class JobTitle(str, Enum):
    Computer_Vision_Researcher = "3D Computer Vision Researcher"
    AI_Scientist = "AI Scientist"
    Analytics_Engineer = "Analytics Engineer"
    Applied_Data_Scientist = "Applied Data Scientist"
    Applied_Machine_Learning_Scientist = "Applied Machine Learning Scientist"
    BI_Data_Analyst = "BI Data Analyst"
    Big_Data_Architect = "Big Data Architect"
    Big_Data_Engineer = "Big Data Engineer"
    Business_Data_Analyst = "Business Data Analyst"
    Cloud_Data_Engineer = "Cloud Data Engineer"
    Computer_Vision_Engineer = "Computer Vision Engineer"
    Computer_Vision_Software_Engineer = "Computer Vision Software Engineer"
    Data_Analyst = "Data Analyst"
    Data_Analytics_Engineer = "Data Analytics Engineer"
    Data_Analytics_Lead = "Data Analytics Lead"
    Data_Analytics_Manager = "Data Analytics Manager"
    Data_Architect = "Data Architect"
    Data_Engineer = "Data Engineer"
    Data_Engineering_Manager = "Data Engineering Manager"
    Data_Science_Consultant = "Data Science Consultant"
    Data_Science_Engineer = "Data Science Engineer"
    Data_Science_Manager = "Data Science Manager"
    Data_Scientist = "Data Scientist"
    Data_Specialist = "Data Specialist"
    Director_of_Data_Engineering = "Director of Data Engineering"
    Director_of_Data_Science = "Director of Data Science"
    ETL_Developer = "ETL Developer"
    Finance_Data_Analyst = "Finance Data Analyst"
    Financial_Data_Analyst = "Financial Data Analyst"
    Head_of_Data = "Head of Data"
    Head_of_Data_Science = "Head of Data Science"
    Head_of_Machine_Learning = "Head of Machine Learning"
    Lead_Data_Analyst = "Lead Data Analyst"
    Lead_Data_Engineer = "Lead Data Engineer"
    Lead_Data_Scientist = "Lead Data Scientist"
    Lead_Machine_Learning_Engineer = "Lead Machine Learning Engineer"
    ML_Engineer = "ML Engineer"
    Machine_Learning_Developer = "Machine Learning Developer"
    Machine_Learning_Engineer = "Machine Learning Engineer"
    Machine_Learning_Infrastructure_Engineer = "Machine Learning Infrastructure Engineer"
    Machine_Learning_Manager = "Machine Learning Manager"
    Machine_Learning_Scientist = "Machine Learning Scientist"
    Marketing_Data_Analyst = "Marketing Data Analyst"
    NLP_Engineer = "NLP Engineer"
    Principal_Data_Analyst = "Principal Data Analyst"
    Principal_Data_Engineer = "Principal Data Engineer"
    Principal_Data_Scientist = "Principal Data Scientist"
    Product_Data_Analyst = "Product Data Analyst"
    Research_Scientist = "Research Scientist"
    Staff_Data_Scientist = "Staff Data Scientist"


app = FastAPI(title="Data Science jobs salary API")


df = pd.read_csv('data/ds_salaries.csv', index_col=0)
df = df.drop_duplicates()
df = df.drop(['salary', 'salary_currency'], axis = 1)
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
async def salary_range_for_job(job_title: JobTitle, company_location: CompanyLocation = None, 
                                     experience_level: ExperienceLevel = None, 
                                     employment_type: EmploymentType = None):
  
    return get_salary_range_for_job(job_title, company_location, experience_level, employment_type)







# load the saved model
model = load('models/GRB_regressor.joblib')

CAT_FEATURES = ['work_year', 
            'experience_level', 
            'employment_type',
            'job_title',
            'employee_residence',
            'remote_ratio',
            'company_location',
            'company_size'
           ]

def encode_data(df):
    # to keep the mapping dictionaries
    category_mappings = dict()
    df_encoded = df.copy()
    for col in CAT_FEATURES:
        df_encoded[col] = df[col].astype('category')
        df_encoded[col] = df_encoded[col].cat.codes
        category_mappings[col] = dict(enumerate(df[col].astype('category').cat.categories))
    return df_encoded, category_mappings

_, category_mappings = encode_data(df)


def apply_existing_encoding(df, category_mappings):
    df_encoded = df.copy()
    for col, mapping in category_mappings.items():
        cat_to_code = {v: k for k, v in mapping.items()}
        df_encoded[col] = df_encoded[col].map(cat_to_code).fillna(-1).astype(int)
    return df_encoded



@app.get("/predict_salary")
async def predict_salary(
    experience_level: ExperienceLevel,
    employment_type: EmploymentType,
    job_title: JobTitle,
    employee_residence: EmployeeResidence,
    remote_ratio: RemoteRatio,
    company_location: CompanyLocation,
    company_size: CompanySize,
    work_year: int = Query(..., ge=2020, le=2022)
):
    
    
    # create a DataFrame from the input data
    X = pd.DataFrame({'work_year': [work_year],
     'experience_level': [experience_level],
     'employment_type': [employment_type],
     'job_title': [job_title],
     'employee_residence': [employee_residence],
     'remote_ratio': [remote_ratio],
     'company_location': [company_location],
     'company_size': [company_size]})
    
    # encode input data to pass to the model
    X_encoded = apply_existing_encoding(X, category_mappings)

    # make a prediction
    prediction = model.predict(X_encoded)
    
    # return the prediction
    return {"result": prediction[0]}


import uvicorn
if __name__=='__main__':
    uvicorn.run("api:app", host="0.0.0.0", reload=False)