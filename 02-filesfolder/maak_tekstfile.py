import io
bestand = open("test4.txt", "w")
bestand.write("test 123!");
bestand.close()

bestand2 = open("test4.txt", "r")
bestand2.write('lekker alles overschrijven')