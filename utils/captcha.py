import random
import base64
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def generate_captcha():
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    captcha = "".join(random.choices(characters, k=4))

    # Generate the captcha image
    image = Image.new("RGB", (120, 50), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype(font=None, size=36)
    draw.text((20, 10), captcha, font=None, fill=(0, 0, 0))

    # Convert the image to base64
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    base64_image = "data:image/png;base64," + base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    return captcha, base64_image
