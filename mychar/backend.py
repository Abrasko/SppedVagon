import os
from uuid import uuid4, uuid3
# from enc_keys import IMG_STORAGE_KEY


def path_and_rename(instance, filename):
    # key = IMG_STORAGE_KEY
    key = uuid4()
    path = 'charimg'
    user_name = instance.photo_author.user_name
    ext = filename.split('.')[-1]
    user_folder = uuid3(key, user_name).hex[:15]
    rand_folder = uuid4().hex[:10]
    filename = '{}.{}'.format(uuid4().hex[:10], ext)
    return os.path.join(path, user_folder, rand_folder, filename)
