from flask import Flask, request, jsonify

app = Flask(__name__)

xeno_table = {
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'TAA':'_','TAG':'_','TGA':'_'
}

flip_thing = {'A':'T','T':'A','C':'G','G':'C','U':'A'}

@app.route('/dna', methods=['POST'])
def chaos_dna():
    blobfish = request.json['seq'].upper()

    kind = "RNA" if 'U' in blobfish else "DNA"

    comp = ''.join(flip_thing.get(x, x) for x in blobfish)
    rev = comp[::-1]

    mrna = blobfish.replace('T','U')

    protein = ""
    for i in range(0, len(blobfish)-2, 3):
        codon = blobfish[i:i+3]
        protein += xeno_table.get(codon, '?')

    return jsonify({
        "type": kind,
        "mrna": mrna,
        "protein": protein,
        "complement": comp,
        "reverse": rev
    })

if __name__ == '__main__':
    app.run(debug=True)