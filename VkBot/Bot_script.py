import vk_api

# Авторизация токена
token = 'vk1.a.rDtakXd_bdWRm6zmTiyDotrtoyhrvgtgJTHXFqRm5NO7qWXrqR7z7aW6RDN0E9kdaNEjSqLgOKJeVBUY3eJbFew0RTYepiJJk7pS6KS9EkEaFsHmNFi3NIkW7Fl8q2z0jVIKWPmWIPQVWCztOrcSfbcA_5FKOJOY1Pz9xsFtthSHhnXaQps1A3Nkd4xY2ZPOVSsUA1oAGqW3alp-oeZmWw'

vk = vk_api.VkApi(token=token)

#Обработка сообщений
message = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered', })

#print(message['items'][0]['last_message'])

#id пользователя
id_l = message['items'][0]['last_message']['from_id']

#id сообщения
id_m = message['items'][0]['last_message']['id']
'''while True:
    messages = vk.method('message.getConversations', {'count': 20, 'filter': 'unanswered', })
    if messages['count'] >= 1:
        print(messages)'''
vk_get_api = vk.longpoll.VkLongPoll(vk)

