import clickhouse_driver
import redis
import requests
import json

# Подключение к базе данных ClickHouse
client = clickhouse_driver.Client('localhost')

# Подключение к Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)


def search_user():
    # Чтение очереди задач на поиск из Redis
    queue = r.lrange('search_queue', 0, -1)
    for task in queue:
        task_data = json.loads(task)
        ipv4 = task_data['ipv4']
        mac = task_data['mac']

        # Осуществление поиска username в ClickHouse
        result = client.execute('SELECT username FROM users WHERE ipv4 = %s AND mac = %s', (ipv4, mac))
        if result:
            # Отправка результирующего JSON во внешний сервис
            data = {
                'username': result[0],
                'ipv4': ipv4,
                'mac': mac
            }
            response = requests.post('https://pastebin.com/api/api_post', json=data)
            if response.status_code == 200:
                url = response.json()['url']

                # Сохранение url на результат успешного поиска в файл
                with open('search_results.txt', 'a') as file:
                    file.write(url + '\n')
        else:
            print('Username not found for ipv4: {} and mac: {}'.format(ipv4, mac))


if __name__ == "__main__":
    search_user()
