# Проект "Вычислитель отличий" 


## Описание
Вычислитель отличий – программа, которая определяет разницу между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн-сервисов, например, jsondiff. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменений в конфигурационных файлах.

## Возможности утилиты
Поддержка разных входных форматов: yaml, json

Генерация отчета в виде plain text, stylish и json

## Установка игр сразу в систему

```sh
make install
```
```sh
make build
```
```sh
make package-install
```
## Usage

```sh
gendiff -f format path/to/file1 path/to/file2
```
## Examples
```sh
gendiff example_files/file1.json example_files/file2.json
```
```sh
gendiff -f plain example_files/file1.json example_files/file2.json
```
```sh
gendiff -f json example_files/file1.json example_files/file2.json
```

### Hexlet tests and linter status:
[![Actions Status](https://github.com/NevermoreKatana/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/NevermoreKatana/python-project-50/actions) <a href="https://codeclimate.com/github/NevermoreKatana/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/dab58b38c4e5848d84b2/maintainability" /></a> <a href="https://codeclimate.com/github/NevermoreKatana/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/dab58b38c4e5848d84b2/test_coverage" /></a> [![My test](https://github.com/NevermoreKatana/python-project-50/actions/workflows/python-app.yml/badge.svg)](https://github.com/NevermoreKatana/python-project-50/actions/workflows/python-app.yml)

[![asciicast](https://asciinema.org/a/DWVtWVXc96utrDKMabUw4YTK9.svg)](https://asciinema.org/a/DWVtWVXc96utrDKMabUw4YTK9)

[![asciicast](https://asciinema.org/a/77lfdli1lAZGxT2bQBHXxohpU.svg)](https://asciinema.org/a/77lfdli1lAZGxT2bQBHXxohpU)

[![asciicast](https://asciinema.org/a/3gBnHcFm5qO0Oog7dh66pRtSR.svg)](https://asciinema.org/a/3gBnHcFm5qO0Oog7dh66pRtSR)

[![asciicast](https://asciinema.org/a/98KVxJYSDjDOarm5CBOo7xAsm.svg)](https://asciinema.org/a/98KVxJYSDjDOarm5CBOo7xAsm)
