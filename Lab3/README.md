# Лабораторна робота №3 — Flask Blueprints

Персоналізований Flask-сайт Євгенія Вербицького з темною зеленою темою.

## Запуск локально

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Render

- Root Directory: `Lab3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Маршрути

- `/` — головна
- `/resume` — резюме
- `/contacts` — контакти
- `/users/hi/Євгеній?age=20` — привітання
- `/users/admin` — перенаправлення
- `/products/` — список товарів
- `/products/1` — деталі товару

Фотографію з оригінального архіву збережено без змін.
