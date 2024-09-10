from flask import Flask, render_template, request
from util import Item, Knapsack

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    inputs = [("", "", ""), ("", "", "")] # Inicializar a tabela com 2 linhas
    capacity = 0
    result = []

    if request.method == "POST":
        capacity = int(request.form.get('capacity', 0))

        names = request.form.getlist('name[]')
        times = request.form.getlist('time[]')
        rates = request.form.getlist('rate[]')
        inputs = [(name, time, rate) for name, time, rate in zip(names, times, rates) if name or time or rate]

        # Criando a mochila
        knapsack = Knapsack(capacity)

        # Cria um array de itens para os itens registrados e não nulos
        items = [Item(name, int(time), int(rate)) for name, time, rate in inputs if name and time and rate]
        # Add itens na mochila
        knapsack.add_items(items)

        # Encontra a solução
        result = knapsack.find_solution()
    
    return render_template("home.html", result=result, inputs=inputs, capacity=capacity)

if __name__ == "__main__":
    app.run(debug=True)
