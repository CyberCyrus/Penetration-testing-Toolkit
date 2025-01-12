def validate_ip(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts)
