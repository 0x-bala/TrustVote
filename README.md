Digital India Blockchain Voting System
📌 Overview
A secure, transparent, and tamper-proof online voting system built on blockchain technology with Aadhaar-based authentication. This system ensures one vote per voter by verifying Aadhaar numbers and recording votes on an immutable blockchain ledger.

✨ Key Features
✅ Aadhaar Verification – Ensures only eligible voters can participate.
✅ One-Vote-Per-Voter – Prevents duplicate voting using hashed Aadhaar storage.
✅ Blockchain Integrity – Votes are recorded in an immutable blockchain.
✅ Real-Time Results – Live vote counting with progress bars.
✅ Secure & Private – Aadhaar numbers are hashed (SHA-256) for privacy.

🛠️ Tech Stack
Category	Technology Used
Backend	Python (Flask)
Blockchain	Custom Python Blockchain
Database	SQLite (for Aadhaar hashes)
Frontend	HTML5, CSS3, Jinja2 Templating
Security	SHA-256 Hashing, Session Management
🚀 Setup & Installation
Prerequisites
Python 3.8+

pip (Python package manager)

Step 1: Clone the Repository
bash
Copy
git clone https://github.com/yourusername/digital-india-voting.git
cd digital-india-voting
Step 2: Install Dependencies
bash
Copy
pip install -r requirements.txt
Step 3: Run the Application
bash
Copy
python app.py
Open http://localhost:5000 in your browser.

📂 Project Structure
Copy
digital-india-voting/  
├── app.py                # Flask backend & routes  
├── blockchain.py         # Blockchain implementation  
├── database.py           # Aadhaar verification & SQLite setup  
├── requirements.txt      # Python dependencies  
├── static/  
│   ├── style.css         # Styling for the web app  
│   └── images/           # Logos & icons (Indian emblem, etc.)  
└── templates/  
    ├── index.html        # Main voting interface  
    └── aadhaar.html      # Aadhaar verification page  
🔐 Security Measures
🔹 Aadhaar Hashing – Stored as SHA-256 hashes (never plain text).
🔹 Session Management – Flask sessions track authenticated voters.
🔹 Blockchain Immutability – Votes cannot be altered once recorded.

📜 License
This project is licensed under MIT License.

📸 Screenshots
(Add screenshots of the voting interface, Aadhaar verification, and results page.)

💡 Future Improvements
OTP-based Aadhaar verification (via UIDAI API)

Multi-language support (Tamil & regional languages)

Voter analytics dashboard

Mobile app integration

🌟 Star & Contribute
If you find this project useful, ⭐ star it on GitHub and feel free to contribute!

🔗 GitHub Link: https://github.com/0x-bala/TrustVote

Made with ❤️ for Digital India 🇮🇳
