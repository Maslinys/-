Ответ на задание 1.
1. Компонентная схема контейнеров:
- Разрабатываем Docker образ с необходимыми зависимостями и настройками для запуска приложения на Python 2.7.
- Используем готовый Docker образ с Redis, настраиваем его под нужды приложения.
- Создаем Docker образ с MySQL, настраиваем на репликацию master-master.
- Используем готовый Docker образ с Apache, настраиваем под нужды приложения.
- Используем готовый Docker образ с Nginx, настраиваем его для обратного проксирования.

Декомпозиция с точки зрения отказоустойчивости:
- Каждый компонент (приложение, Redis, MySQL, Apache, Nginx) размещается в отдельном контейнере, что позволяет изолировать их друг от друга. Если один компонент упадет, другие продолжат работать, обеспечивая более высокий уровень отказоустойчивости.

2. Описание образов необходимых контейнеров:
- Для каждого компонента создаем Dockerfile, в котором описываем шаги по сборке Docker образа для этого компонента. В Dockerfile указываем базовый образ, устанавливаем необходимое ПО, копируем конфигурационные файлы и настраиваем окружение для запуска контейнера.

3. Подробное описание процесса развертывания на новом хосте:
- Устанавливаем Docker на новом хосте, следуя официальной документации в соответствии с версией Ubuntu, в нашем случае Ubuntu 18.04.5.
- Для каждого компонента собираем Docker образ с помощью команды "docker build" и Dockerfile, описывающего этот образ.
- Создаем файл docker-compose.yml, описывающий конфигурацию и взаимодействие контейнеров.
- Запускаем контейнеры, используя команду "docker-compose up".


Ответ на задание 2 + python код.
1. Развертывание ClickHouse:
   - Установить ClickHouse на сервер.
   - Создать таблицу в ClickHouse с полями username, ipv4, mac.
   - Наполнить таблицу сгенерированными данными.

2. Реализация сервиса поиска учетной записи:
   - Использовать Python 2.7+ для написания сервиса.
   - Использовать Redis для хранения очереди задач на поиск.
   - Реализовать логику сервиса, который читает задачи из очереди, осуществляет поиск в ClickHouse по ipv4 и mac, отправляет результат во внешний сервис и сохраняет URL результата в файл.
   - Обеспечить параллельную обработку очереди для повышения производительности.
   - Учесть корнер кейсы, такие как недоступность СУБД или внешнего сервиса, и обработать их адекватно.
