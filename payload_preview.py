"""Show the exact Technocore payload string before signing.

This does not load identity.pem and does not create a signature.
"""

def normalize(text: str) -> str:
    return " ".join(text.strip().split())

def main() -> None:
    room = input("Room [lobby]: ").strip() or "lobby"
    nonce = input("Nonce [1001]: ").strip() or "1001"
    message = input("Message: ").strip() or "Hello from a new Technocore contributor"
    payload = f"{room}|{nonce}|{normalize(message)}"
    print()
    print("Exact payload that gets signed:")
    print(payload)
    print()
    print("Flow: message -> normalize -> room|nonce|text -> Ed25519 sign -> Technocore")

if __name__ == "__main__":
    main()
