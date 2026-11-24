# Lab9 — Євгеній Вербицький

Windows / VS Code, з папки Lab9:

```powershell
py -m pip install -r requirements.txt
py -m flask --app run db upgrade
py seed_lab9.py
py -m flask --app run run
```

http://127.0.0.1:5000/users/register — створіть новий тестовий обліковий запис.
Попередні автори залишені для постів; їх випадкові паролі не призначені для входу.

Тести: `py -m unittest discover -s tests -p test_auth.py -v`

Render: Root Directory `Lab9`, Build Command `pip install -r requirements.txt`, Start Command `flask --app run db upgrade && python seed_lab9.py && gunicorn run:app`. Задайте SECRET_KEY у Environment. Без постійного диска SQLite та завантажені файли можуть втрачатися при перезапуску.
