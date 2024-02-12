## ATS_APPLICATION
### Application Tracking System based on Job description related to data science job profile
### Application is trained using Google gemini pro pre-trained model.
### Prompting job description and uploading resume gives the specific result such as:
#### 1. Tell me about resume
#### 2. Percentage Match

### Create API KEY
``
Create .env file and add GOOGLE_API_KEY
visit https://makersuite.google.com/app/apikey website and create API Key and store in .env file
``
### created a environment using Annaconda
```Bash
conda create -p "venv" python==3.8 -y
```
### activate environment
```Bash
conda activate venv/
```
### Install all necessary libraries
```Bash
pip install -r requirements.txt
```
## To run the application
```bash
streamlit run app.py
```
