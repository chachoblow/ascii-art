from PIL import Image, ImageDraw, ImageFont

# Convert image into an Image object, resize, and create array for pixels.
im = Image.open("neemz.jpg")
im.resize((400, 300))
imageAr = [[] for y in range(im.height)]

for y in range(im.height):
    imageAr[y] = [im.getpixel((x, y)) for x in range(im.width)]

# Create brightness value array.
brightnessAr  = [[] for y in range(im.height)]

# Set each element in the brightness array to the brightness of the corresponding pixel in the Image array.
for y in range(im.height):
    brightnessAr[y] = [(0.21 * imageAr[y][x][0] + 0.72 * imageAr[y][x][1] + 0.07 * imageAr[y][x][2]) for x in range(im.width)]

# Characters to be used for drawing. In order of ascending 'darkness'.
characters = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")

scalar = (len(characters) - 1) / 254.0

charAr = [[] for y in range(im.height)]

# Rescale the brightness values.
for y in range(im.height):
    charAr[y] = list(map(lambda x: int(round(x * scalar)), brightnessAr[y]))

newCharAr = [[] for y in range(im.height)]

# Set the characters.
for y in range(im.height):
    for x in range(im.width):
        charAr[y][x] = str(characters[charAr[y][x]] * 2)

for y in range(im.height):
    print("".join(charAr[y]))
