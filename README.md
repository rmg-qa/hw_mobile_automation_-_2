# Mobile Automation # 2
Установка зависимостей  
pip install -r requirements.txt  
Реализованы автотесты: в эмуляторе "Android Studio", на реальном устройстве, в "Browserstack"    

_Важно!_   
Перед запуском автотестов необходимо:
1) В корень проекта добавить последнюю версию приложения "wikipedia.apk"
2) Необходимо на локальной машине развернуть сервер с помощью команды "appium" в PowerShell - иначе автотесты на эмуляторе и реальном устройстве не запустятся
3) Создать файл .env и положить его в корень проекта


Структура файла .env выглядит так:  
BROWSERSTACK_USERNAME=<Ваш USER_ID в Browserstack>  
BROWSERSTACK_ACCESS_KEY=<Ваш Accesskey в Browserstack>  
BROWSERSTACK_PROJECT_NAME=<Необязательный параметр>  
BROWSERSTACK_BUILD_NAME=<Необязательный параметр>  
BROWSERSTACK_SESSION_NAME=<Необязательный параметр>  

Запуск автотестов в Browserstack на Windows:  
$env:CONTEXT="bstack"; pytest <Ваш путь до тестов>  

Запуск автотестов локально на эмуляторе на Windows:  
_Необходимо изменить параметр udid устройства и REMOTE_URL (путь до сервера на локальной машине), который лежит в .env.local_emulator_   
$env:CONTEXT="local_emulator"; pytest <Ваш путь до тестов>  

Запуск автотестов локально на реальном устройстве на Windows:  
_Необходимо изменить параметр udid устройства и REMOTE_URL (путь до сервера на локальной машине), который лежит в .env.local_real_  
$env:CONTEXT="local_real"; pytest <Ваш путь до тестов>  

Запуск Allure-отчета:  
allure serve allure-results
