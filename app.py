from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        wish = request.form.get("wish")
        if wish:
            message = "Terima kasih atas doa & ucapannya!"

    data = {
        "groom": "M. Fatahul Alim Tohir",
        "groom_parents": "Bapak Tohirin & Ibu Kartinah",
        "bride": "Fadhilatul Laili",
        "bride_parents": "Bapak Ustadz Muhammad Yahya & Ibu Ustadzah Siti Maesaroh",
        "akad_date": "Ahad, 12 Oktober 2025 • 09.00 WIB",
        "akad_venue": "Masjid Baitul Mustajabah, Kota Tegal",
        "resepsi_date": "Ahad, 12 Oktober 2025 • 11.00 WIB - selesai",
        "resepsi_venue": "Jl. Brawijaya Rt 04/ Rw 02 Muarareja, Kota Tegal",
        "gallery": ["gambar1.jpg", "gambar2.jpg", "gambar3.jpg"],
        "bank_accounts": [
            {"type": "Bank Jateng", "number": "1234567890", "name": "Ayu Wulandari"},
            {"type": "DANA", "number": "081234567890", "name": "Ayu Wulandari"},
            {"type": "ShopeePay", "number": "081234567890", "name": "Bagus Santoso"}
        ]
    }
    
    nama_tamu = request.args.get('to', 'Tamu Undangan')

    return render_template("index.html", data=data, nama_tamu=nama_tamu, message=message)

if __name__ == "__main__":
    app.run(debug=True)