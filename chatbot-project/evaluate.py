import argparse
from chatbot import load_corpus, build_index, search

def main():
    parser = argparse.ArgumentParser(description="Evaluate chatbot with sample queries")
    parser.add_argument('--data_dir', required=True, help="Directory with .txt files")
    args = parser.parse_args()
    
    # Load and index corpus
    try:
        documents, doc_metadata = load_corpus(args.data_dir)
        vectorizer, tfidf_matrix = build_index(documents)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Test queries
    queries = [
        "What is artificial intelligence?",
        "Who is Sherlock Holmes?",
        "What is machine learning?",
        "Pride and Prejudice plot",
        "Applications of AI"
    ]
    
    print("Running evaluation...")
    for query in queries:
        try:
            best_match, top3_results = search(query, vectorizer, tfidf_matrix, doc_metadata)
            print(f"\nQuery: {query}")
            if best_match:
                print(f"Best Match: {best_match['para'][:100]}... (Score: {best_match['score']:.2f})")
                print("Top-3 Matches:")
                for i, result in enumerate(top3_results, 1):
                    print(f"{i}. {result['file']}: {result['para'][:50]}... (Score: {result['score']:.2f})")
            else:
                print("No relevant matches found.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()