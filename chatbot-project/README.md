# Offline TF-IDF Chatbot

This project implements a simple **offline chatbot** that retrieves relevant paragraphs from local text files using **TF-IDF** and **cosine similarity**. It does not require an internet connection and can answer questions based on the provided data.

---

## Project Structure

chatbot-project/
│
├── chatbot.py            # Main chatbot code
├── requirements.txt      # Python dependencies
├── README.md             # Project instructions
├── provenance.md         # Sources of text data
├── data/                 # Folder containing .txt files
│   ├── ai_wiki.txt
│   ├── ml_wiki.txt
│   ├── sherlock_holmes.txt
│   ├── pride_and_prejudice.txt
│   └── tech_blog.txt
└── outputs/              # Folder containing logs
    └── session.jsonl

---

## Dependencies

- Python 3.x
- NLTK
- scikit-learn
- numpy

Install dependencies using:

pip install -r requirements.txt

---

## How to Run

1. Activate your virtual environment (if using venv):

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

2. Install dependencies:

pip install -r requirements.txt

3. Place your `.txt` files in the `data/` folder.

4. Run the chatbot:

python chatbot.py --data_dir ./data

5. Enter queries or type `quit` / `exit` to stop the chatbot.

---

## Example Queries

- What is artificial intelligence?  
- Explain machine learning.  
- Who is Sherlock Holmes?  
- Tell me about Pride and Prejudice  
- What is data analysis?  

---

## Output

All interactions are logged in:

outputs/session.jsonl

Each entry records:

- `query` — User input  
- `top1` — Best matching paragraph and score  
- `top3` — Top-3 matching paragraphs and scores  
- `timestamp` — When the query was made
