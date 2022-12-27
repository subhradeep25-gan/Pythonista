from PIL import Image
from captcha.image import ImageCaptcha

# The size of your captcha
image = ImageCaptcha(width = 300, height = 100)
# The text you wish to generate a captcha
captcha_text = input("Enter the captcha text: ")
#saving the image
image.write(captcha_text, 'Captcha.png')
Image.open('Captcha.png')