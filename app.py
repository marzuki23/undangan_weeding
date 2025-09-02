from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Path to store RSVP data
RSVP_FILE = 'rsvp_data.json'

def load_rsvps():
    """Loads RSVP data from a JSON file."""
    if os.path.exists(RSVP_FILE):
        with open(RSVP_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupted JSON file
                return []
    return []

def save_rsvps(rsvps):
    """Saves RSVP data to a JSON file."""
    with open(RSVP_FILE, 'w') as f:
        json.dump(rsvps, f, indent=4)

@app.route("/", methods=["GET"])
def index():
    data = {
        "groom": "M. Fatahul Alim Tohir",
        "groom_parents": "Bapak Tohirin & Ibu Kartinah",
        "bride": "Fadhilatul Laili",
        "bride_parents": "Alm. Bapak Muhammad Yahya & Ibu Siti Maesaroh",
        "akad_date": "Ahad, 12 Oktober 2025 • 09.00 WIB",
        "akad_venue": "Masjid Baitul Mustajabah, Kota Tegal",
        "resepsi_date": "Ahad, 12 Oktober 2025 • 10.00 WIB - selesai",
        "resepsi_venue": "Jl. Brawijaya Rt 04/ Rw 02 Muarareja, Kota Tegal",
        "gallery": ["gambar 1.jpg", "gambar 2.jpg", "gambar 3.jpg"], # Pastikan gambar ini ada di static/img
        "bank_accounts": [
            {"type": "Bank Jateng", "number": "3158030160", "name": "Fadhilatul Laili"},
            {"type": "DANA", "number": "082323939692", "name": "Afiyatussyaadah"},
            {"type": "ShopeePay", "number": "082323939692", "name": "Afiyatussya adah"},
        ]
    }
    
    nama_tamu = request.args.get('to', 'Tamu Undangan')

    return render_template("index.html", data=data, nama_tamu=nama_tamu)

@app.route("/rsvp", methods=["POST"])
def rsvp():
    try:
        data = request.get_json()
        guest_name = data.get('guest_name')
        attendance = data.get('attendance')
        num_guests = data.get('num_guests')
        message = data.get('message')

        if not guest_name or not attendance or not num_guests:
            return jsonify({"success": False, "message": "Harap lengkapi semua bidang yang wajib diisi (Nama, Kehadiran, Jumlah Tamu)."}), 400

        rsvps = load_rsvps()
        
        # Add a timestamp to the RSVP entry
        timestamp = datetime.now().isoformat()

        new_rsvp = {
            "timestamp": timestamp,
            "guest_name": guest_name,
            "attendance": attendance,
            "num_guests": int(num_guests), # Ensure num_guests is an integer
            "message": message
        }
        rsvps.append(new_rsvp)
        save_rsvps(rsvps)

        return jsonify({"success": True, "message": "Terima kasih! Konfirmasi kehadiran Anda telah terkirim."}), 200

    except Exception as e:
        print(f"Error processing RSVP: {e}")
        return jsonify({"success": False, "message": "Terjadi kesalahan saat memproses konfirmasi Anda. Silakan coba lagi."}), 500

if __name__ == "__main__":
    app.run(debug=True)