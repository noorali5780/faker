import random
import time
import hashlib
from datetime import datetime, timedelta
from faker import Faker
from colorama import Fore, Style, init
from pypinyin import lazy_pinyin

# Initialize colorama for colored terminal output
init(autoreset=True)
fake = Faker('zh_CN')  # Chinese locale

email_domains = ['gmail.com', 'outlook.com', 'qq.com', 'protonmail.com', '163.com']

def generate_chinese_name():
    name = fake.name()
    return name

def name_to_pinyin(name):
    return ''.join(lazy_pinyin(name))

def generate_email(username_pinyin):
    return f"{username_pinyin}{random.randint(10,99)}@{random.choice(email_domains)}"

def generate_password_hash():
    raw_pass = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$', k=12))
    hash_obj = hashlib.sha256(raw_pass.encode())
    return hash_obj.hexdigest()

def generate_dob():
    start_date = datetime.strptime('1975-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2005-01-01', '%Y-%m-%d')
    dob = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return dob.strftime('%Y-%m-%d')

def generate_ip():
    return f"{random.randint(36,123)}.{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def hacker_banner():
    banner = f"""
{Fore.GREEN}
 █████╗ ██╗███████╗██╗  ██╗ █████╗ ███╗   ███╗███████╗
██╔══██╗██║██╔════╝██║ ██╔╝██╔══██╗████╗ ████║██╔════╝
███████║██║███████╗█████╔╝ ███████║██╔████╔██║█████╗  
██╔══██║██║╚════██║██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══╝  
██║  ██║██║███████║██║  ██╗██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
{Style.RESET_ALL}
    """
    print(banner)

def main():
    hacker_banner()
    try:
        while True:
            name = generate_chinese_name()
            pinyin_username = name_to_pinyin(name)
            email = generate_email(pinyin_username)
            password_hash = generate_password_hash()
            dob = generate_dob()
            ip = generate_ip()

            print(Fore.RED + "[密码已找到] " + Style.RESET_ALL + "Leak detected:")
            print(Fore.YELLOW + f" > Name: {name}")
            print(f" > Username (pinyin): {pinyin_username}")
            print(f" > Email: {email}")
            print(f" > Password (sha256): {password_hash}")
            print(f" > Date of Birth: {dob}")
            print(f" > IP Address: {ip}")
            print(Fore.CYAN + "-" * 50 + Style.RESET_ALL)

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nExiting leak simulator...")

if __name__ == "__main__":
    main()
