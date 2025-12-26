# Импортируем необходимые модули
from flask import Flask, render_template
import random  # Для генерации случайных комплиментов

# Инициализируем Flask-приложение
app = Flask(__name__)

# Список комплиментов
compliments = [
    "Ты сегодня невероятно красив(а)!",
    "Ты вдохновляешь всех вокруг!",
    "Ты делаешь мир ярче и добрее!",
    "Ты очень талантлив(а) и уникален(на)!",
    "Ты лучший(ая) — не забывай об этом!",
    "Твоя улыбка освещает всё вокруг!",
    "Ты заслуживаешь самого лучшего!",
    "Ты сильный(ая) и смелый(ая)!",
    "Ты умный(ая) и находчивый(ая)!",
    "Ты — источник позитива!"
]

# Главная страница
@app.route("/")
def home():
    # Передаём случайный комплимент в шаблон
    return render_template("index.html", compliment=random.choice(compliments))

# Запускаем приложение, если этот файл запущен напрямую
if __name__ != "__main__":
    from gevent.pywsgi import WSGIServer
    port = int(os.environ.get("PORT", 5000))
    server = WSGIServer(("0.0.0.0", port), app)
    server.serve_forever()
