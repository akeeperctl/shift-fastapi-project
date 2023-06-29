# Shift FastAPI project
REST-сервис, где по логину и паролю сотрудника выдаётся секретный токен, по которому можно получить данные о зарплате и дату следующего повышения этого сотрудника.

## Возможности сервиса
- Добавление/удаление/изменение пользователей (**суперпользователь**);
- Добавление/удаление/изменение рабочих позиций (**суперпользователь**);
- Верификация учетной записи;
- Просмотр сведений о зарплате и о дате следующего повышения;
- Просмотр сведений о других пользователях (**суперпользователь**).

## Стэк технологий
- **PostgreSQL** как база данных;
- **Redis** как хранилище для токенов и кэширования;
- **Poetry** для сбора зависимостей и быстрой их установки;
- **Docker Compose** для создания и использования контейнеров сервиса;
- **FastAPI** как ядро сервиса;
- **Pytest** для написания тестов.
- **PyCharm** как среда разработки

## Установка и запуск сервиса
1. Скопировать репозиторий к себе на рабочую машину
2. С помощью **PyCharm** создать и активировать виртуальную среду **Python 3.11**. 
Обязательно должен быть **(venv)** в начале пути командной строки. Это означает, что вирт. среда активирована

    ```sh
    (venv) PS C:\project\shift-fastapi-project-main 
    ```
3. Установить **Poetry** используя **pip**
    ```sh
    pip install Poetry
    ```
4. Проверить правильность установки **Poetry**
    ```sh
    poetry --version
    ```
5. Установить все зависимости с помощью **Poetry**
    ```sh
    poetry install
    ```
6.  Настроить файл **.env** под себя.
    > Примечание:
    > Файл `.env-non-dev` используется для работы приложения через Docker контейнеры

    ```sh
    # Значения базы данных
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=shift-project-db
    DB_USER=postgres
    DB_PASS=postgres
    
    # Значения базы данных, которая 
    # используется при прогоне тестов
    DB_HOST_TEST=localhost
    DB_PORT_TEST=5432
    DB_NAME_TEST=shift-project-test-db
    DB_USER_TEST=postgres
    DB_PASS_TEST=postgres
    
    # Настройка Редиса
    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_STRATEGY_LIFETIME=600 # sec
    
    # Ваш секретное слово. Может быть любым.
    # Храните его в недоступном месте.
    # Используется в JWT токенах
    SECRET=secretary_secret
    
    # Время жизни токенов
    TOKEN_RESET_PASSWORD_LIFETIME=120
    TOKEN_VERIFICATION_LIFETIME=300
    
    # Определяет будет ли при старте сервиса создаваться рабочее место "заглушка" в БД
    CREATE_PLUG_JOB=True
    ```
7. Запустить сервер базы данных и сервер хранилища Redis
8. Запустить сервер с помощью **uvicorn**
    ```sh
    uvicorn src.main:app
    ```

    ```
    # Вот что должно быть при успешном запуске
    INFO:     Started server process [12732]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```
9. Проверить сервис по адресу http://127.0.0.1:8000/docs

## Тестирование
Прогнать тесты можно с помощью команды **pytest**
```sh
pytest -s -v .\tests 
```

## Docker
Проект поддерживает сборку контейнеров с помощью Docker Compose. Инструкция как собрать и запустить контейнеры для сервиса и баз данных.
Обязательно внутри проекта должны находиться файлы **Dockerfile** и **docker-compose.yaml**

#### Сборка образа через Docker
1.  Ввести команду для создания образа
    ```sh
    docker build . -t shift-project-image:latest
    ```
    > Примечание: 
    Где `shift-project-image` там может быть Ваше название. 
    Где `latest` там может быть Ваша версия.
2.  Создать контейнер из полученного образа. В настройках контейнера указать порт для подключения с вашей машины в формате **хххх:yyyy**. 
Где `хххх` - порт на вашей машине, `yyyy` - порт Docker'а.

#### Сборка образов через Docker Composer
1.  Ввести команду для создания образов
    ```sh
    docker compose build
    ```

    ```sh
    # Печатается после команды...
    [+] Building 0.2s (2/3)
     => [app internal] load .dockerignore                                               
    [+] Building 0.3s (2/3)
    [+] Building 7.0s (15/15) FINISHED
     => [app internal] load .dockerignore   
     
    # Успешно
    => [app] exporting to image                                                             
    => => exporting layers                                                              
    => => writing image sha256:3547069b9552a7da3f65dfe308d87a71de68de3c61e4d9167с
    => => naming to docker.io/library/shift-fastapi-project-app  
    ```
2.  Ввести команду для создания и запуска контейнеров
    ```sh
    docker compose up
    ```
    > Будут созданы образы сервиса, базы данных, редиса и сеть для них.
    После чего автоматически будут созданы и запущены контейнеры.
    
3.  Проверить все запущенные контейнеры
    - **Базы данных** по умолчанию используют порт 5433:5432. Где `5433` - это порт, по которому можно подключиться к БД с вашего компьютера, например используя **pgAdmin** или любую другую программу. А `5432` нужен для общения базы данных и приложения между контейнерами.
    - **Redis** по умолчанию использует 6380:6379
    - **REST-сервис** по умолчанию использует 3000:8000. Во время авторизации в поле `username` нужно вводить почту
    