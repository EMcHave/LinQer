# Телеграм бот - хранитель ссылок

Данный бот написан для того, чтобы сохранять ссылки на инетересующие вас источники, которые вы не можете изучить сейчас,
но в будущем с удовольствием бы изучили. Описание функционала будет показано после введении команды /start.
Эта команда и позволяет начать взаимодействие с ботом. После введения этой команды вы увидете:

```
Привет! Я бот, который поможет не забыть прочитать статьи, найденные тобой в интернете :)
- Чтобы я запомнил статью, достаточно передать мне ссылку на нее. К примеру https://example.com
- Чтобы получить случайную статью, достаточно передать мне команду /get_article.
Но помни! Отдавая статью тебе на прочтение, она больше не хранится в моей базе.Так что тебе точно нужно её изучить
```

Исчерпывающее описание, остается только опробовать его на практике :D

link: https://t.me/linqer_bot

## Установка ПО для запуска бота

1. Установить интерпретатор python версии 3.11 или выше.
2. В папке с файлами приложения создать виртуальное окружение с помощью консольной команды python -m venv {venv name}, после чего активировать его командой venv\Scripts\activate.bat для Windows или source venv/bin/activate для Linux и MacOS.
3. Установить требуемые библиотеки в активированное виртуальное окружение командой pip install -r requirements.txt.
4. Зарегестрировать своего бота в [телеграм у Отца Ботов](https://t.me/BotFather).
5. Получить API_TOKEN и присвоить его одноименной переменной в файле main.py в формате API_TOKEN = "ваш_api_token".
6. Для запуска бота введите команду python main.py в консоли.
