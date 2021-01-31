# shop_tests
Selenium Python

[![Build Status](https://travis-ci.org/berpress/shop_tests.svg?branch=main)](https://travis-ci.org/berpress/shop_tests)

#**Pre-commit-hooks**
##Необходимо установить pre-commit:
`pip install pre-commit`
##Далее следует выполнить команду:
`pre-commit install`
##Принудительный запуск pre-commit:
`pre-commit run --all-files`
##Запуск определенного hook:
`pre-commit run <hook_id> <options>`
+ [hook-id]: необходимо указать единственный идентификатор
  ловушки для запуска;
+ -a, --all-files: запустить все файлы в репозитории;
+ --files [FILES[FILES...]]: запустить для файла с
  конкретным именем.


#**Allure**
**Необходимо установить scoop. В powershell выполнить две команды:**

1) Set-ExecutionPolicy RemoteSigned -scope CurrentUser
2) Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')

**Устанавливаем Allure с помощью команды:**

scoop install allure


Необходимо проверить, установлена ли Java. Для этого ввести allure
и нажать enter. Если не установлена, то необходимо установить и добавить в
переменные окружения.

**Запустить тесты с allure(в терминале IDE):**

pytest --alluredir <dir_name>

**Открыть отчёт(в powershell, нужно находиться в той папке, где лежит <dir_name>):**

allure serve <dir_name>
