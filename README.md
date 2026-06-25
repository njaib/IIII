# 🤖 ربات اسکرین‌شات تلگرام

این ربات تلگرام با دریافت لینک از کاربر، از آن سایت اسکرین‌شات گرفته و عکس را برای کاربر ارسال می‌کند.

---

## 🔧 ابزارهای مورد نیاز (چه چیزهایی باید نصب کنی؟)

### 1. نصب Python (نسخه 3.8 یا بالاتر)
- اگر ویندوز داری: از [python.org](https://www.python.org/downloads/) دانلود و نصب کن.
- اگر لینوکس/مک داری: معمولاً نصب هست. با دستور `python3 --version` چک کن.

> ⚠️ موقع نصب روی ویندوز حتماً گزینه **"Add Python to PATH"** را تیک بزن.

---

### 2. نصب Google Chrome (مرورگر)
برای گرفتن اسکرین‌شات به مرورگر Chrome نیاز داری.

- **ویندوز/مک**: از [google.com/chrome](https://www.google.com/chrome/) دانلود و نصب کن.
- **لینوکس (اوبونتو/دبیان)**:
  ```bash
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
  sudo apt-get update
  sudo apt-get install google-chrome-stable