from imgurpython import ImgurClient
from decouple import config

from imgurpython import ImgurClient

client_id = config('IMGUR_CLIENT_ID')
client_secret = config('IMGUR_CLIENT_SECRET')
album_id = config('IMGUR_ALBUM_ID')


client = ImgurClient(client_id, client_secret)

# get image links from gallery
items = client.get_album_images(album_id)
for item in items:
    print(item.link)
