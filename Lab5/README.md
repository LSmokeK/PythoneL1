# Лабораторна робота №5 — Flask

Проєкт Євгенія Вербицького. Темна тема із зеленими акцентами, Flask-WTF форми, TinyDB каталог товарів, авторизація та сторінка резюме.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Render

- Root Directory: `Lab5`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn run:app`
- Environment: `SECRET_KEY` = випадковий довгий секретний рядок

У каталозі є два навчальні товари: Lenovo LOQ 15 та Razer DeathAdder V3. Ціни демонстраційні. Оригінальні фото товарів вилучено з карток, щоб не показувати зображення інших моделей. Завантаження зображень працює через форму додавання/редагування.

**Увага:** TinyDB і завантажені фото зберігаються у файловій системі. На безкоштовному Render локальні зміни можуть губитися після перезапуску/розгортання.
