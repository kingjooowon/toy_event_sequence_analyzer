def build_sequences(events):
    grouped = {}
    
    for e in events:
        user = e["user_id"]
        
        if user not in grouped:
            grouped[user] = []
            
        grouped[user].append(e)
        
    sequences = {}
    
    for user, evs in grouped.items():
        evs.sort(key=lambda x: x["timestamp"])
        sequences[user] = [e["event"] for e in evs]