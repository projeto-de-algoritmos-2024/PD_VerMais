from flask import Flask, render_template, request
from util import Item, Knapsack 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    inputs = [("", "", ""), ("", "", "")] 
    capacity = 0
    result = []

    if request.method == "POST":
        names = request.form.getlist('name[]')
        times = request.form.getlist('time[]')
        rates = request.form.getlist('rate[]')
        capacity = int(request.form.get('capacity', 0))

        inputs = [(name, time, rate) for name, time, rate in zip(names, times, rates) if name or time or rate]

        
        knapsack = Knapsack(capacity)
        items = [Item(name, int(time), int(rate)) for name, time, rate in inputs if name and time and rate]
        knapsack.add_all_items(items)

        
        knapsack.solve()
        result = knapsack.find_solution()
    
    return render_template("home.html", result=result, inputs=inputs, capacity=capacity)

if __name__ == "__main__":
    app.run(debug=True)
