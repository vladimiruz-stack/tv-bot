import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

PROGRAMS = [
    "Клара Румянова. Звезда за кадром",
    "НТВ. Дни творения",
    "Перо и шпага Валентина Пикуля",
    "Эдуард Хиль - Сто хитов короля эстрады",
    "Гоголь и ляхи",
    "Кремлёвские похороны. Лаврентий Берия",
    "Сеанс с Кашпировским",
    "Тайны сновидений",
    "Экстрасенсы",
    "Сумашествие",
    "Оборотни",
    "Волльвебер. Личный враг Гитлера",
    "Спето в СССР. Госпожа удача",
    "Сталин и писатели",
    "Уроки пения",
    "Владимир Володин. Опереточный герой",
    "Николай Гумилев. Завещание",
    "Никулин и Шуйдин",
    "Алексей Попов. Трагедия в трех актах с прологом и эпилогом",
    "В поисках Франции с Вадимом Глускером",
    "Тайны лазурного берега",
    "Последняя капля",
    "Маленькое черное платье",
    "Снять по-французски",
    "Хранители наследства",
    "Другая жизнь Натальи Шмельковой",
    "Исторические путешествия с Иваном Толстым",
    "Стрит-Арт. Философия прямого действия",
    "Мировые леди",
    "Проявления Павла Каплевича",
    "Последний тусовщик Оттепели",
    "Вначале было дело или История русской промышленности",
]

CHANNELS = [
    "Культура",
    "Первый канал",
    "НТВ",
    "Россия",
    "Мир",
]

SEARCH_URL = "https://tv.yandex.ru/search?text="

def send_telegram(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text},
        timeout=20
    )

def check_program(title):
    url = SEARCH_URL + requests.utils.quote(title)
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20).text
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)

    found_channel = next((ch for ch in CHANNELS if ch in text), None)

    if found_channel:
        return f"Нашёл возможный эфир:\n«{title}»\nКанал: {found_channel}\n{url}"

    return None

def main():
    results = []

    for title in PROGRAMS:
        result = check_program(title)
        if result:
            results.append(result)

    if results:
        send_telegram("\n\n---\n\n".join(results))
    else:
        print("Эфиров пока не найдено.")

if __name__ == "__main__":
    main()
