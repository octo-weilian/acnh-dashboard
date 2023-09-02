from src import *
from sqlalchemy.schema import MetaData
from sqlalchemy.schema import CreateTable

def format_prompt(question,engine):
	meta = MetaData()
	meta.reflect(bind=engine)
	tables =  '\n\n'.join([ str(CreateTable(table)).replace('\n','').replace('\t','').replace('"','') for table in meta.sorted_tables ])

	return '\n\n'.join([tables,
					   "--Using valid SQL, answer the following questions for the tables provided above.",
					   f"--{question}",
					   "SELECT"])
    
def question_to_nsql(question,engine,hf_api_key):
	prompt = format_prompt(question,engine)
	payload = {"inputs": prompt,"parameters":{"temperature":0.2,"max_new_tokens":100},"options":{'use_cache':'false'}}
	headers = {"Authorization": f"Bearer {hf_api_key}"}
	API_URL = "https://api-inference.huggingface.co/models/NumbersStation/nsql-350M"
	with requests.post(API_URL, headers=headers, json=payload) as r:
		data = r.json()
		try:
			return data[0]['generated_text'].split('\n\n')[-1]
		
		except:
			return data
		