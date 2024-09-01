import qrcode
import os
from PIL import Image

def load_items_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            items = file.read().splitlines()
            return items
    except FileNotFoundError:
        print(f"Soubor '{filename}' nebyl nalezen.")
        return []

def generate_unique_filename(base_path, base_name, extension):
    counter = 0
    file_name = f"{base_name}{extension}"
    file_path = os.path.join(base_path, file_name)

    while os.path.exists(file_path):
        counter += 1
        file_name = f"{base_name}{counter:02d}{extension}"
        file_path = os.path.join(base_path, file_name)

    return file_path

def create_qr_code(text, box_size=10, output_size=None):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )
    qr.add_data(text, optimize=0)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    if output_size:
        img = img.resize((output_size, output_size), Image.LANCZOS)

    return img

file_path = input("Zadejte cestu k souboru se seznamem položek: ")

items_in_box = load_items_from_file(file_path)

if not items_in_box:
    print("Soubor je prázdný nebo nebyl nalezen.")
else:
    text = "\n".join(items_in_box)

    size_choice = input("Chcete nastavit velikost QR kódu pomocí (1) velikosti boxu nebo (2) celkové velikosti obrázku? Zadejte 1 nebo 2: ")

    if size_choice == '1':
        box_size = int(input("Zadejte velikost boxu (doporučeno 1-40, výchozí je 10): ") or 10)
        img = create_qr_code(text, box_size=box_size)
    elif size_choice == '2':
        output_size = int(input("Zadejte celkovou velikost QR kódu v pixelech: "))
        img = create_qr_code(text, output_size=output_size)
    else:
        print("Neplatná volba. Použije se výchozí velikost.")
        img = create_qr_code(text)

    downloads_folder = os.path.expanduser("~/Downloads")
    output_file = generate_unique_filename(downloads_folder, "qr_code", ".png")

    img.save(output_file)

    print(f"QR kód byl úspěšně vygenerován a uložen jako {output_file}.")