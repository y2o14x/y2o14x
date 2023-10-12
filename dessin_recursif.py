import transgeo as tg
from PIL import Image, ImageDraw

def vk(profondeur, A, B, **kwargs):
    if profondeur == 0:
        CTX.line([A, B], **kwargs)
        return
    #
    C = tg.homothetie(B, A, 1/3)
    E = tg.homothetie(B, A, 2/3)
    D = tg.rotation60(E, C)
    vk(profondeur - 1, A, C, **kwargs)
    vk(profondeur - 1, C, D, **kwargs)
    vk(profondeur - 1, D, E, **kwargs)
    vk(profondeur - 1, E, B, **kwargs)

W = 800
img = Image.new("RGB", (W, 300))
CTX = ImageDraw.Draw(img)

vk(3, (0, 0), (W - 1, 0), width=5)
img.save("vk.png")
img.show()
