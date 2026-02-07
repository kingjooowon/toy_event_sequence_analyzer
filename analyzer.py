import os, json
from collections import Counter
from reader import read_events
from sequence import build_sequences
from anomaly import detect_anomalies
from report import generate_report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample_events.csv")

def count_sequences(sequences):
    counter = Counter()
    
    for seq in sequences.values():
        if not seq:
            continue
        
        key = "->".join(seq)
        counter[key] += 1
        
    return dict(counter)

def main():
    events = read_events("sample_events.csv")
    sequences = build_sequences(events)
    sequence_counts = count_sequences(sequences)
    anomalies = detect_anomalies(sequences)
    
    generate_report(
        total_users=len(sequences),
        sequence_counts=sequence_counts,
        anomalies=anomalies
    )
    
    result = {
        "total_users" : len(sequences),
        "top_sequences" : sequence_counts,
        "anomalies" : anomalies 
    }
    
    print("\nJSON 결과:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
if __name__ == "__main__":
    main()