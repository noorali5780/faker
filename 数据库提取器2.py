import random
import time
import hashlib
from datetime import datetime, timedelta
from faker import Faker
from colorama import Fore, Style, init
from pypinyin import lazy_pinyin

# Init
init(autoreset=True)
fake = Faker('zh_CN')
email_domains = ['gmail.com', 'outlook.com', 'qq.com', 'protonmail.com', '163.com']

log_file_path = "数据库提取器.txt"

def generate_chinese_name():
    return fake.name()

def name_to_pinyin(name):
    return ''.join(lazy_pinyin(name))

def generate_email(username_pinyin):
    return f"{username_pinyin}{random.randint(10, 99)}@{random.choice(email_domains)}"

def generate_password():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$', k=12))

def generate_password_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_dob():
    start_date = datetime.strptime('1975-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2005-01-01', '%Y-%m-%d')
    dob = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return dob.strftime('%Y-%m-%d')

def generate_ip():
    return f"{random.randint(36,123)}.{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def generate_phone():
    return f"1{random.choice([3, 5, 7, 8, 9])}{random.randint(100000000, 999999999)}"

def luhn_checksum(card_number):
    def digits_of(n): return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def generate_credit_card_number():
    prefix = random.choice(['622202', '622848', '356833', '622700'])  # UnionPay prefixes
    num = prefix + ''.join(random.choices('0123456789', k=9))
    for i in range(10):
        trial = num + str(i)
        if luhn_checksum(trial) == 0:
            return trial
    return num + '0'

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

def log_to_file(data_str):
    with open(log_file_path, "a", encoding="utf-8") as file:
        file.write(data_str + "\n")

def main():
    hacker_banner()
    try:
        while True:
            name = generate_chinese_name()
            pinyin_username = name_to_pinyin(name)
            email = generate_email(pinyin_username)
            password = generate_password()
            password_hash = generate_password_hash(password)
            dob = generate_dob()
            ip = generate_ip()
            phone = generate_phone()
            cc_number = generate_credit_card_number()

            output = (
                f"[密码已找到] Leak Detected:\n"
                f" > Name: {name}\n"
                f" > Username (pinyin): {pinyin_username}\n"
                f" > Email: {email}\n"
                f" > Phone: +86-{phone}\n"
                f" > Date of Birth: {dob}\n"
                f" > Password: {password}\n"
                f" > Password Hash (sha256): {password_hash}\n"
                f" > Credit Card #: {cc_number}\n"
                f" > IP Address: {ip}\n"
                f"{'-' * 60}"
            )

            print(Fore.RED + "[密码已找到] " + Style.RESET_ALL + "Leak Detected:")
            print(Fore.YELLOW + f" > Name: {name}")
            print(f" > Username (pinyin): {pinyin_username}")
            print(f" > Email: {email}")
            print(f" > Phone: +86-{phone}")
            print(f" > Date of Birth: {dob}")
            print(f" > Password: {password}")
            print(f" > Password Hash (sha256): {password_hash}")
            print(f" > Credit Card #: {cc_number}")
            print(f" > IP Address: {ip}")
            print(Fore.CYAN + "-" * 60 + Style.RESET_ALL)

            log_to_file(output)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nExiting leak simulator...")

if __name__ == "__main__":
    main()
