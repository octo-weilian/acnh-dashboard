# ACNH Dashboard

### Features
- Home
- Catalog
- Chart
- Chatbot
<p align="center">
  <img width="600" style="border-radius:5%;box-shadow: rgba(149, 157, 165, 0.5) 0px 8px 24px" src="images/chatbot.png">
</p>

### Note
- Chatbot uses the Huggingface (free) inference API and [NumbersStation/nsql-350M](https://huggingface.co/NumbersStation/nsql-350M)

### Quick start
1. Copy this repo
2. Create and activate Python virtual environment
```bash
python3 -m venv .venv && source .venv/bin/activate
``` 
3. Install Python requirements
```bash
pip install -r requirements.txt
``` 
4. Run Postgres container
```bash
docker compose up -d --build
``` 
5. Run Streamlit
```bash
streamlit run Home.py
``` 

