# Лабораторна №7 — Зв’язки. Міграції

**Автор:** Євгеній Вербицький. На основі попередньої лабораторної №6.

## Що реалізовано
- SQLAlchemy-моделі `Category` та `Product` зі зв’язком один-до-багатьох.
- `naming_convention` для обмежень.
- Міграції додавання `Product`, `Category`, `active`, `created_at` та ручна міграція даних.
- Приклади товарів: Lenovo LOQ 15 та Razer DeathAdder V3.
- Збережено сторінки й дизайн попередньої роботи та пост про GTA VI.

## Локальний запуск
```bash
pip install -r requirements.txt
flask --app run db upgrade
python seed_gta6.py
python run.py
```
Не запускайте `flask db init` повторно: каталог `migrations` уже є.

## Для перевірки та скріншотів
```bash
flask --app run db current
flask --app run db history
flask --app run db check
```
Відкрийте `instance/data.sqlite` у DB Browser for SQLite. Зробіть скріншоти таблиць `products` і `categories`, їхніх даних та історії міграцій. Для тесту відкату використовуйте лише копію бази.

## Render
Root Directory: `Lab7` (якщо папку завантажено в корінь GitHub-репозиторію).
Build Command: `pip install -r requirements.txt && flask --app run db upgrade && python seed_gta6.py`
Start Command: `gunicorn run:app`
Задайте `SECRET_KEY` в Environment. На безкоштовному Render SQLite-файли не мають постійного сховища, тому зміни можуть втрачатися після redeploy.

**Примітка:** інтерфейс товарів попередньої лабораторної використовує TinyDB. Моделі та міграції SQLAlchemy реалізовані окремо відповідно до лабораторної №7. Це дві різні бази; для повного переходу інтерфейсу на SQLAlchemy потрібне додаткове переписування CRUD.
