import qrcode

# Seznam věcí v krabici
items_in_box = [
    "Zimní kabát",
    "Lyžařské rukavice",
    "Vánoční ozdoby",
    "Stan"
]

# Vytvoření textového seznamu
text = "\n".join(items_in_box)

# Vygenerování QR kódu
qr = qrcode.QRCode(
    version=1,  # verze QR kódu
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # úroveň korekce chyb
    box_size=10,  # velikost boxu
    border=4,  # tloušťka okraje
)
qr.add_data(text)
qr.make(fit=True)

# Vytvoření obrázku QR kódu
img = qr.make_image(fill="black", back_color="white")
img.save("qr_code.png")  # uloží QR kód jako obrázek

print("QR kód byl úspěšně vygenerován a uložen jako qr_code.png.")