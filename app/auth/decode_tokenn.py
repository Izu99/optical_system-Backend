from jose import JWTError, jwt

SECRET_KEY = "your_secret_key"  # Replace with the actual key used during encoding
ALGORITHM = "HS256"

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print(f"JWT decoding error: {e}")
        raise

if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2MCwicm9sZSI6Im93bmVyIiwiYnJhbmNoX2lkIjoxNiwic2hvcF9pZCI6MiwiZXhwIjoxNzIzMzc2NTY2fQ.a9mz-DF5AR9i3ikJxfDoVs1fOZXZZ1sWlCZkh-KE7BE"

    try:
        decoded_data = decode_token(token)
        print(f"Decoded token data: {decoded_data}")

        if 'role' in decoded_data:
            print(f"Role from token: {decoded_data['role']}")
        else:
            print("Role is not present in the token.")
    except JWTError as e:
        print(f"Error decoding token: {e}")
