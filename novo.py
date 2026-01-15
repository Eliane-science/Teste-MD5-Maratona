import hashlib
import string

base_link = "https://forms.layers.education/xL9tB4{}E0RzVp7KfG2{}hU?answ=79d7f16"
hash_correto = "3793c8078310d6035c9483d65d1ed0be"

caracteres = string.ascii_letters + string.digits  

for c1 in caracteres:
    for c2 in caracteres:
        link_testado = base_link.format(c1, c2)
        md5 = hashlib.md5(link_testado.encode()).hexdigest()

        if md5 == hash_correto:
            print("Você encontrou!")
            print("Caracteres encontrados:", c1, c2)
            print("Link completo:", link_testado)
            exit()
