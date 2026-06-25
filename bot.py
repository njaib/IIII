import os
import time
from pyrogram import Client, filters
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PIL import Image

# =====================================================
# 🔑 جای قرار دادن توکن ربات و لینک سایت (همین جاست)
# =====================================================

# 1️⃣ توکن ربات خودت را اینجا بذار (از @BotFather گرفتی)
BOT_TOKEN = "7561653912:AAFo4bZ-tyZC6HRPCYekjiSFlf96Aq7unyc"

# 2️⃣ لینک سایتی که می‌خوای اسکرین‌شات بگیری (می‌تونی تغییرش بدی)
TARGET_URL = "https://khorasantelecom.co/"

# 3️⃣ API_ID و API_HASH رو از my.telegram.org بگیر
API_ID = 1234567  # ← عدد API_ID خودت رو بذار
API_HASH = "abcdef1234567890"  # ← رشته API_HASH خودت رو بذار

# =====================================================
# مسیر ChromeDriver (اگه در PATH نیست، مسیر کامل رو بذار)
CHROMEDRIVER_PATH = "chromedriver.exe"  # ویندوز
# CHROMEDRIVER_PATH = "/usr/bin/chromedriver"  # لینوکس
# =====================================================

app = Client(
    "screenshot_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def get_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1280,720")
    chrome_options.add_argument("--disable-gpu")
    
    try:
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        time.sleep(5)
        
        screenshot_path = f"screenshot_{int(time.time())}.png"
        driver.save_screenshot(screenshot_path)
        
        img = Image.open(screenshot_path)
        img = img.resize((1280, 720))
        img.save(screenshot_path)
        
        driver.quit()
        return screenshot_path
        
    except Exception as e:
        print(f"خطا: {e}")
        return None

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 سلام! به ربات اسکرین‌شات خوش آمدی.\n\n"
        f"🔹 لینک پیش‌فرض: {TARGET_URL}\n"
        "📤 برای گرفتن اسکرین‌شات، دکمه زیر رو بزن یا لینک دیگه‌ای بفرست."
    )

@app.on_message(filters.text & ~filters.command("start"))
async def take_screenshot(client, message):
    url = message.text.strip()
    
    # اگه کاربر فقط پیام داد و لینک نفرستاد، از لینک پیش‌فرض استفاده کن
    if not url.startswith("http://") and not url.startswith("https://"):
        url = TARGET_URL
        await message.reply_text(f"🔁 از لینک پیش‌فرض استفاده می‌شود: {url}")
    
    waiting_msg = await message.reply_text("⏳ در حال گرفتن اسکرین‌شات... لطفاً صبر کن.")
    
    screenshot_path = get_screenshot(url)
    
    if screenshot_path and os.path.exists(screenshot_path):
        await message.reply_photo(
            photo=screenshot_path,
            caption=f"✅ اسکرین‌شات از: {url}"
        )
        os.remove(screenshot_path)
    else:
        await message.reply_text("❌ خطا در گرفتن اسکرین‌شات. لطفاً دوباره تلاش کن.")
    
    await waiting_msg.delete()

print("🤖 ربات اسکرین‌شات روشن شد...")
app.run()