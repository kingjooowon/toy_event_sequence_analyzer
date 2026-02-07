def detect_anomalies(sequences):
    result = {
        "no_login_purchase": [],
        "no_view_cart": [],
        "short_session" : []
    }
    
    for user, seq in sequences.items():
        if "purchase" in seq and "login" not in seq:
            result["no_login_purchase"].append(user)
        
        if "add_to_cart" in seq and "view" not in seq:
            result["no_view_cart"].append(user)
            
        if len(seq) <= 2:
            result["short_session"].append(user)
            
    return result