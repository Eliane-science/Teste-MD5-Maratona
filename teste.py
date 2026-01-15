import hashlib

link = "https://forms.layers.education/xL9tB4sE0RzVp7KfG2QhU?answ=79d7f16"

hash_md5 = hashlib.md5(link.encode()).hexdigest()

print(hash_md5)
