# shop_tests

Selenium Python

[![Build Status](https://travis-ci.org/berpress/shop_tests.svg?branch=main)](https://travis-ci.org/berpress/shop_tests)

# **Pre-commit-hooks**

## Необходимо установить pre-commit:

`pip install pre-commit`

## Далее следует выполнить команду:

`pre-commit install`

## Принудительный запуск pre-commit:

`pre-commit run --all-files`

## Запуск определенного hook:

`pre-commit run <hook_id> <options>`

+ [hook-id]: необходимо указать единственный идентификатор ловушки для запуска;
+ -a, --all-files: запустить все файлы в репозитории;
+ --files [FILES[FILES...]]: запустить для файла с конкретным именем.

# **Формирование HTML-отчёта с помощью pytest-html**

## Установить pytest-html:

 `pip install pytest-html`

###### **pytest-html будет работать с Python >=3.6 или PyPy3**

## Для создания отчёта запустить тесты командой:

`pytest --html=report.html --self-contained-html
`

#### **О редактировании внешнего вида отчёта можно почитать подробнее [https://pytest-html.readthedocs.io/en/latest/user_guide.html#creating-a-self-contained-report][тут]**


[тут]: https://pytest-html.readthedocs.io/en/latest/user_guide.html#creating-a-self-contained-report
