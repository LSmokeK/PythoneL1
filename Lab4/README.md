# Лабораторна робота №4 — Flask

Персоналізований навчальний сайт Євгенія Вербицького: темний стиль із зеленими акцентами, резюме, каталог, Flask Blueprints, сесії, авторизація, cookie та профіль.

## Локальний запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Render

Root Directory: `Lab4`
Build Command: `pip install -r requirements.txt`
Start Command: `gunicorn run:app`

Додайте змінну оточення `SECRET_KEY` з довгим випадковим значенням у Render → Environment.

Навчальний логін: `user1`, пароль: `12345`. Це демонстраційна авторизація, не для реальних облікових записів.
