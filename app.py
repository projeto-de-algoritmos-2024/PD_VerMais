from flask import Flask, render_template, request
# import utils

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    inputs = [("", "", ""), ("", "", ""), ("", "", "")]  # Inicializa com três linhas vazias

    if request.method == "POST":
        names = request.form.getlist('name[]')  # Obtém todos os valores do campo name[]
        times = request.form.getlist('time[]')  # Obtém todos os valores do campo time[]
        rates = request.form.getlist('rate[]')  # Obtém todos os valores do campo rate[]
        
        inputs = [(name, time, rate) for name, time, rate in zip(names, times, rates) if name or time or rate]

        # Todo: Criar um objeto de knapsack com os valores names e values
        # Todo: Atribuir a result os valores result = knapsack.selected()
        result = f"Você enviou: {inputs}"  # Exemplo para mostrar os pares name-time-rate
        
    else:
        result = "Nada"

    return render_template("home.html", result=result, inputs=inputs)

if __name__ == "__main__":
    app.run(debug=True)
