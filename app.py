import os
from flask import *
import hamiltonian

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        clauses = request.form.get('clauses',False,type=str)
        if(not clauses):
            return render_template('index.html',clausula = clauses,hamiltonianpath="Escriba una clausula")
        hamiltonianpath = hamiltonian.main(str(clauses))
        return render_template('index.html',clausula = clauses,hamiltonianpath = hamiltonianpath )
    else:
        return render_template('index.html',hamiltonianpath="Escriba una clausula")
	
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8081)),debug=True)
