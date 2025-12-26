def calculate_zone_health(bin_data):
    weighted_sum = 0
    total_weight = 0

    for bin in bin_data:
        weighted_sum += bin["fill_level"] * bin["confidence"]
        total_weight += bin["confidence"]

    return weighted_sum / total_weight if total_weight else 0
