import vk
import time
import sys

session = vk.AuthSession(sys.argv[1], sys.argv[2], sys.argv[3], scope = 'status')
vk_api = vk.API(session)
while 1 == 1:
    now = time.localtime(time.time() + 3600 * 3)
    vk_api.status.set(text = "Сегодня: " + str(now[2] // 10) + str(now[2] % 10) + '.' + str(now[1] // 10) + str(now[1] % 10) + '.' + str(now[0]) + ". Время: " + str(now[3] // 10) + str(now[3] % 10) + ':' + str(now[4] // 10) + str(now[4] % 10) + '.')
    time.sleep(60 - now[5])
