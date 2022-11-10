from PIL import Image

afbeelding = Image.open("maliqenlion.jpg")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("de afbeelding is" + str(breedte) + " pixels breed en " + str(hoogte) + "pixels hoogte ")

print(afbeelding.format, afbeelding.size, afbeelding.mode)