def optimize_route(zones):
    priority = sorted(zones, key=lambda z: z["health"], reverse=True)
    return [zone["name"] for zone in priority]
