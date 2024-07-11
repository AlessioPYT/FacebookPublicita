import json

foto_publicita = 'c:/Users/Алексей/Downloads/Screenshot+2024-07-11+103952.png'
insert_text = '//div[@class="x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]'
groups = "https://www.facebook.com/groups/feed/"
enter_all = '//div[@aria-label="Отправить"]'
publication_create = '//div[@aria-label="Создайте общедоступную публикацию…"]'
foto_video_button = '//div[@aria-label="Фото/видео"]'
add_foto = '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]'
some_groups = {
    1: "https://www.facebook.com/groups/1781014825372492/", 
    2: "https://www.facebook.com/groups/parloitalianoetu", 
    3: "https://www.facebook.com/groups/smilesofworld"
}
some_text = {1: "hello", 2: "whats Up", 3: "Hey Guys"}



with open("config.json") as config_file:
    config = json.load(config_file)
login = config["login"]
password = config["password"]