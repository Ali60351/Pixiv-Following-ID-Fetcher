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
    json_result = api.user_following(self_ID, restrict='public', offset=i, req_auth=True)

    for users in json_result['user_previews']:
        user_ids.append(users['user']['id'])
        pass

    if json_result.get('next_url'):
        next_flag = True
        pass
    else:
        next_flag = False
        pass
    pass

    print('Fetched ' + user_ids.__len__().__str__() + ' user IDs')
    i += 30
    pass

with open('List.txt', 'w') as outfile:
    for ids in user_ids:
        outfile.write(ids.__str__() + "\n")
        pass
    pass

print('Fetching complete')