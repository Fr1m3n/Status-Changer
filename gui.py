import vk
import time
import sys

session = vk.AuthSession('6354496', sys.argv[1], sys.argv[2], scope = 'status')
vk_api = vk.API(session)
while 1 == 1:
    now = time.localtime()
    vk_api.status.set(text = "Сегодня: " + str(now[2] // 10) + str(now[2] % 10) + '.' + str(now[1] // 10) + str(now[1] % 10) + '.' + str(now[0]) + ". Время: " + str(now[3] // 10) + str(now[3] % 10) + ':' + str(now[4] // 10) + str(now[4] % 10) + '.')
    time.sleep(60 - now[5])
