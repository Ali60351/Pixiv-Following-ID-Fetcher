from pixivpy3 import *

api = AppPixivAPI()
username = input('Enter Username: ')
password = input('Enter Password: ')
self_ID = int(input('Enter own member ID: '))

api.login(username, password)

i = 0
user_ids = []
next_flag = True

while next_flag:
    json_result = api.user_following(self_ID, offset=i)

    for users in json_result['user_previews']:
        user_ids.append(users['user']['id'])

    if json_result.get('next_url'):
        next_flag = True
    else:
        next_flag = False

    print(f'Fetched {len(user_ids)} user IDs')
    i += 30

with open('List.txt', 'w') as outfile:
    for ids in user_ids:
        outfile.write(str(ids) +  "\n")

print('Fetching complete')
