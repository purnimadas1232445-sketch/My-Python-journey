import requests
from bs4 import BeautifulSoup

# ১. ইনপুট: আসল লাইভ লিংক যেখানে ডাটা সাজানো আছে
url = "https://scrapethissite.com"

# ২. প্রসেস: পাইথন রিকোয়েস্ট পাঠিয়ে ওয়েবসাইট থেকে সব তথ্য ফোনে আনছে
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("--- 🌍 লাইভ ডাটা আনা হচ্ছে এবং ডাউনলোড ফোল্ডারে সেভ করা হচ্ছে ---")
print("=" * 60)

# ৩. লজিক: ওয়েবসাইটের ভেতর থেকে সব ডাটা বক্স খুঁজে বের করা
countries = soup.find_all('div', class_='col-md-4 country')

# 🎯 মাস্টার ট্রিক: ফাইলটি অন্য কোথাও না রেখে সরাসরি ফোনের মেইন 'Download' ফোল্ডারে তৈরি করা
with open("/storage/emulated/0/Download/client_result.txt", "w", encoding="utf-8") as file:
    
    file.write("=== ক্লায়েন্টের জন্য স্ক্র্যাপ করা লাইভ ডাটা লিস্ট ===\n\n")
    
    count = 0
    for country in countries:
        if count >= 5: # আমরা প্রথম ৫টি দেশের ডাটা ফাইলে নেব
            break
            
        # নাম, রাজধানী এবং জনসংখ্যা স্ক্র্যাপ করার লজিক
        name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text.strip()
        population = country.find('span', class_='country-population').text.strip()
        
        # ডাটাগুলো সরাসরি ফাইলে রাইট (Write) বা সেভ করা
        file.write(f"দেশ {count+1}: {name}\n")
        file.write(f"রাজধানী: {capital}\n")
        file.write(f"জনসংখ্যা: {population}\n")
        file.write("-" * 40 + "\n")
        
        count += 1

print("=" * 60)
print("--- 💸 অভিনন্দন বন্ধু! ফাইলটি সরাসরি 'Download' ফোল্ডারে সেভ হয়েছে! ---")
