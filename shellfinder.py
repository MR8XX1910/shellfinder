import requests

# طباعة البانر
print("""
   _____ __         ___________           __         
  / ___// /_  ___  / / / ____(_)___  ____/ /__  _____
  \__ \/ __ \/ _ \/ / / /_  / / __ \/ __  / _ \/ ___/
 ___/ / / / /  __/ / / __/ / / / / / /_/ /  __/ /    
/____/_/ /_/\___/_/_/_/   /_/_/ /_/\__,_/\___/_/     
                                                     
	""")
print("Shell Finder v0.0.1 by mr.8xx (1945)\n\n")
print("[*] INFO: Websites should start with 'http://' or 'https://' and should not end with '/'")

# تحميل البيانات من الملفات
try:
    with open('websites.txt', 'r') as file:
        websites = [line.strip() for line in file if line.strip()]
    with open('endpoints.txt', 'r') as file:
        endpoints = [line.strip() for line in file if line.strip()]
except FileNotFoundError as e:
    print(f"[-] ERROR: {e}")
    exit()

print("[*] INFO: Searching...")

# الفحص
for website in websites:
    print(f"\n[*] INFO: Target: {website}")
    for endpoint in endpoints:
        url = f"{website}/{endpoint}"
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                print(f"[+] SUCCESS: Shell found at: {url}")
            elif res.status_code == 403:
                print(f"[-] FORBIDDEN: {url}")
            elif res.status_code == 404:
                print(f"[-] NOT FOUND: {url}")
        except requests.exceptions.RequestException as e:
            print(f"[-] ERROR: Could not connect to {url} ({e})")
