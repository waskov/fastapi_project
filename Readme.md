## Для локального запуска требуется:

0) Создать окружение
```bash
python3.11 -m venv env
```
1) В директории активировать окружение
```bash
source env/bin/activate
```
3) Установить библиотеки из requirements.txt
```bash
pip install --no-cache-dir -r requirements.txt
```
4) Запуск через uvicorn
```bash
uvicorn app.app:app --host 0.0.0.0 --port 3000
```

Упаковка в контейнер
```bash
docker build -t fastapi-app .
```
Запуск из контейнера
```bash
docker run -p 3000:3000 fastapi-app
```
Добавь параметр --tty , который позволяет подключить псевдотерминал к контейнеру, что включает поддержку управления цветами и форматирования вывода
```bash
docker run --tty -p 3000:3000 fastapi-app
```

```bash
для локального запуска может потребоваться ngrok (открыть доступ к локальному веб-серверу из интернета)
ngrok http 3000
```