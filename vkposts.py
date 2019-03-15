import vk_api

session = vk_api.VkApi(token = '00d582e400d582e400d582e4bb00bcb620000d500d582e45c53c88eaaab6f6509e2b1a7')
vk = session.get_api()

offset = 0
posts = ''
c = 0

for i in range(0,999):
    data = vk.wall.get(domain = 'meduzaproject',count=50, offset=offset)
    offset += 50
    for i in data['items']:
        print(c,".",i['text'])
        c += 1
        sleep(20)
