x = input("Inserire la larghezza dell'immagine: ")
y = input("Inserire l'altezza dell'immagine: ")

channels = input("inserire il numero dei canali: ")

pixel = int(x)*int(y)*int(channels)


print("larghezza:", x, "\naltezza:", y)
print("numero di pixel totali, ", pixel)

