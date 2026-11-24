from run import app
from app.extensions import db
from app.posts.models import Post, User, Tag
from app.extensions import bcrypt
import secrets
DATA = [
('Grand Theft Auto VI — гра, на яку я чекаю','Мені подобається атмосфера Vice City, великі відкриті світи та можливість досліджувати місто. Від GTA VI я очікую цікавих персонажів, живого міста та захопливого сюжету. Особливо цікаво побачити, як розробники реалізують деталі світу та взаємодію з ним.', 'default.jpg',1,['Ігри','Відкритий світ']),
('Ghost of Tsushima','Події гри відбуваються у феодальній Японії під час монгольського вторгнення. Самурай Дзін Сакай захищає свій острів. Мені подобаються красиві пейзажі, атмосферна музика та бойова система. Дослідження острова дозволяє відкривати нові місця та історії.', 'ghost.jpg',1,['Ігри','Відкритий світ','Пригоди']),
('Dying Light','Гра про виживання у місті, охопленому зомбі-апокаліпсисом. Паркур дозволяє швидко пересуватися дахами та уникати ворогів. Уночі небезпека зростає, тому доводиться планувати свої дії. Мені подобається поєднання свободи пересування та напруженої атмосфери.', 'dying.jpg',2,['Ігри','Відкритий світ','Виживання']),
('Assassin’s Creed Black Flag Resynced','Мене зацікавила піратська тематика оригінальної Black Flag. Морські битви, дослідження островів, пошук скарбів та пригоди Едварда Кенвея створюють особливу атмосферу. Від оновленої версії я очікую покращеної графіки та збереження духу оригіналу.', 'blackflag.jpg',2,['Ігри','Пригоди']),
('Red Dead Redemption 2','Це історія Артура Моргана та банди Ван дер Лінде на заході Америки. Гра вражає деталізованим світом, природою та сильним сюжетом. Мені подобається можливість подорожувати верхи, досліджувати міста і спостерігати за життям персонажів. Особливо запам’ятовується атмосфера Дикого Заходу.', 'rdr2.jpg',1,['Ігри','Відкритий світ','Пригоди'])]
with app.app_context():
    for i,n in [(1,'Євгеній Вербицький'),(2,'Game Reviewer')]:
        if not db.session.get(User,i): db.session.add(User(id=i,username=n,email=f'author{i}@example.invalid',password=bcrypt.generate_password_hash(secrets.token_hex(24)).decode("utf-8")))
    db.session.flush()
    for title,content,image,author_id,names in DATA:
        post=db.session.scalar(db.select(Post).where(Post.title==title))
        if post is None:
            post=Post(title=title,content=content,image=image,author_id=author_id,category='publication',is_active=True)
            db.session.add(post)
            for name in names:
                tag=db.session.scalar(db.select(Tag).where(Tag.name==name))
                if tag is None:
                    tag=Tag(name=name);db.session.add(tag)
                post.tags.append(tag)
    db.session.commit()
    print('Posts:',db.session.scalar(db.select(db.func.count(Post.id))))
