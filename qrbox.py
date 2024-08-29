import qrcode
import os

# Načtení položek ze souboru
def load_items_from_file(filename):
    try:
        with open(filename, 'r') as file:
            items = file.read().splitlines()
            return items
    except FileNotFoundError:
        print(f"Soubor '{filename}' nebyl nalezen.")
        return []

# Vyzvání uživatele k zadání cesty k souboru
file_path = input("Zadejte cestu k souboru se seznamem položek: ")

# Načtení položek ze zadaného souboru
items_in_box = load_items_from_file(file_path)

# Zajištění, aby nebyl seznam prázdný
if not items_in_box:
    print("Soubor je prázdný nebo nebyl nalezen.")
else:
    # Vytvoření textového seznamu
    text = "\n".join(items_in_box)

    # Vygenerování QR kódu
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Cesta k uložení souboru do složky Stahování (Downloads)
    downloads_folder = os.path.expanduser("~/Downloads")
    output_file = os.path.join(downloads_folder, "qr_code.png")

    # Vytvoření obrázku QR kódu
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)  # uloží QR kód jako obrázek do složky Downloads

    print(f"QR kód byl úspěšně vygenerován a uložen jako {output_file}.")
