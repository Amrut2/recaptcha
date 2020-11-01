from captcha.image import ImageCaptcha
import random
import string

def recapp():
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(9))
    image  = ImageCaptcha(width = 250 ,height = 100)
    text = random

    image = image.create_captcha_image("{}".format(result_str),color= "white" , background="black")

    # image.show()
    return image.save("gen1.jpg")

