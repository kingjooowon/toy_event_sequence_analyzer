import os
from collections import Counter
from reader import read_events
from sequence import build_sequences
from anomaly import detect_anomalies

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


if __name__ == "__main__":
    
    events = read_events("sample_events.csv")
    sequences = build_sequences(events)
    stats = count_sequences(sequences)
    anomalies = detect_anomalies(sequences)
    
    print(events)
    print(sequences)
    print(stats)
    print(anomalies)
    