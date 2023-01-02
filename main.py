from instagrapi import Client

print("▪  ▐ ▄.▄▄ ▄▄▄▄▄▄▄▄· ▄▄ •▄▄▄  ▄▄▄·• ▌ ▄ ·.     ▄▄▄▄·    ▄▄▄▄▄")
print("██•█▌▐▐█ ▀•██ ▐█ ▀█▐█ ▀ ▀▄ █▐█ ▀█·██ ▐███▪    ▐█ ▀█▪   •██  ")
print("▐█▐█▐▐▄▀▀▀█▐█.▄█▀▀█▄█ ▀█▐▀▀▄▄█▀▀█▐█ ▌▐▌▐█·    ▐█▀▀█▄▄█▀▄▐█.▪")
print("▐███▐█▐█▄▪▐▐█▌▐█ ▪▐▐█▄▪▐▐█•█▐█ ▪▐██ ██▌▐█▌    ██▄▪▐▐█▌.▐▐█▌·")
print("▀▀▀▀ █▪▀▀▀▀▀▀▀ ▀  ▀·▀▀▀▀.▀  ▀▀  ▀▀▀  █▪▀▀▀    ·▀▀▀▀ ▀█▄▀▀▀▀ ")
print("-------------------------------------------------------------")
print("                       Made by dvx#8583")
print("-------------------------------------------------------------")
username = input("Enter Username: ")
password = input("Enter Password: ")
client = Client()
client.login(username, password)

hashtag = input("Enter Hashtag: ")
amount = int(input("Enter Amount: "))
posts = client.hashtag_medias_recent(hashtag, amount)

for i in range(amount):
    print("Post " + str(i + 1))
    client.media_like(posts[i].id)
    print("Liked post")
    client.user_follow(posts[i].user.pk)
    print("Followed " + posts[i].user.username)
input("Operation Ended, Press enter to close: ")