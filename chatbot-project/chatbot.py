import os
import json
import argparse
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime, timezone

# Download NLTK data (only first time)
nltk.download('punkt', quiet=True)

# ---------------------- Data Loader ----------------------
def load_paragraphs_from_directory(data_dir):
    paragraphs = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Split text into paragraphs
                for para in content.split('\n\n'):
                    clean_para = para.strip()
                    if clean_para:
                        paragraphs.append((filename, clean_para))
    print(f"Loaded {len(paragraphs)} paragraphs from {len(os.listdir(data_dir))} files.\n")
    return paragraphs

# ---------------------- Similarity Search ----------------------
def find_best_match(query, paragraphs, vectorizer, para_vectors):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, para_vectors).flatten()
    top_indices = similarities.argsort()[-3:][::-1]

    top_matches = []
    for idx in top_indices:
        file, para = paragraphs[idx]
        score = similarities[idx]
        top_matches.append({'file': file, 'para': para, 'score': round(float(score), 2)})

    best_match = top_matches[0] if top_matches else {'file': '', 'para': 'No match found', 'score': 0.0}
    return best_match, top_matches

# ---------------------- Logging ----------------------
def log_interaction(query, best_match, top3_results, output_file):
    """Log each chatbot interaction in JSONL format."""
    log_entry = {
        'query': query,
        'top1': best_match if best_match else {'file': '', 'para': 'No match found', 'score': 0.0},
        'top3': top3_results,
        'timestamp': datetime.now(timezone.utc).isoformat()
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry) + '\n')

# ---------------------- Chatbot Main ----------------------
def main(data_dir, output_file='outputs/session.jsonl'):
    paragraphs = load_paragraphs_from_directory(data_dir)

    # Prepare TF-IDF vectorizer
    corpus = [para for _, para in paragraphs]
    vectorizer = TfidfVectorizer(stop_words='english')
    para_vectors = vectorizer.fit_transform(corpus)

    print("Chatbot ready! Enter your query (or 'quit'/'exit' to exit):")

    while True:
        query = input("> ").strip()
        if query.lower() in ('exit', 'quit'):
            print("Goodbye! 👋")
            break

        best_match, top_matches = find_best_match(query, paragraphs, vectorizer, para_vectors)

        print("\nBest Match:")
        print(f"File: {best_match['file']}")
        print(f"Paragraph: {best_match['para'][:300]}{'...' if len(best_match['para']) > 300 else ''}")
        print(f"Score: {best_match['score']}\n")

        print("Top-3 Matches:")
        for i, match in enumerate(top_matches, 1):
            print(f"{i}. File: {match['file']}, Score: {match['score']}")

        # Log to session file
        log_interaction(query, best_match, top_matches, output_file)

# ---------------------- Run Script ----------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple AI Chatbot using TF-IDF similarity")
    parser.add_argument('--data_dir', type=str, required=True, help="Path to directory containing .txt files")
    args = parser.parse_args()

    main(args.data_dir)
