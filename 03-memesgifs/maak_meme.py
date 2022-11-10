
from PIL import Image, ImageFont, ImageDraw
 
lettertype = ImageFont.truetype("impact.ttf",80)


afbeelding = Image.open("meme_background.jpg")
 
afbeelding.show()
 
breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)
 
helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2
 
nieuwe_afmeting = (helft_breedte, helft_hoogte)

lettertype = ImageFont.truetype("impact.ttf",60)
 
tekengebied = ImageDraw.Draw(afbeelding)
 
tekst = "Coding in Python\nNo problemo!"
 
tekengebied.multiline_text((80,100), tekst, font=lettertype, fill=(0,0,0))
 
afbeelding.show()
