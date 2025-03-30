from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from blockchain import Blockchain
import database

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this for production
blockchain = Blockchain()
database.init_db()

@app.route('/')
def index():
    if 'aadhaar_verified' not in session:
        return redirect(url_for('aadhaar_verification'))
    return render_template('index.html', 
                         candidates=blockchain.candidates,
                         chain=blockchain.chain)

@app.route('/aadhaar', methods=['GET', 'POST'])
def aadhaar_verification():
    if request.method == 'POST':
        aadhaar_number = request.form['aadhaar_number']
        
        # Basic Aadhaar validation (12 digits)
        if len(aadhaar_number) != 12 or not aadhaar_number.isdigit():
            return render_template('aadhaar.html', error="Invalid Aadhaar number")
        
        session['aadhaar_verified'] = True
        session['aadhaar_number'] = aadhaar_number
        return redirect(url_for('index'))
    
    return render_template('aadhaar.html')

@app.route('/vote', methods=['POST'])
def vote():
    if 'aadhaar_verified' not in session:
        return redirect(url_for('aadhaar_verification'))
    
    aadhaar_number = session['aadhaar_number']
    candidate = request.form['candidate']
    
    if blockchain.new_vote(aadhaar_number, candidate):
        # Mine a new block
        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        
        previous_hash = blockchain.hash(last_block)
        blockchain.new_block(proof, previous_hash)
        
        return redirect(url_for('index'))
    else:
        return "You have already voted or invalid Aadhaar!", 400

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('aadhaar_verification'))

@app.route('/chain')
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)