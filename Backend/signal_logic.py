def calculate_signal_time(congestion_level):
    base_time = 30  # seconds
    
    if congestion_level <= 2:
        return base_time
    elif congestion_level <= 3:
        return base_time + 20
    elif congestion_level <= 4:
        return base_time + 40
    else:
        return base_time + 60
