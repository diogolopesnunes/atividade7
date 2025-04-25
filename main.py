from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        operacao = request.form.get("operacao")

        resultado = None
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                return render_template("calculadora.html",
                                       erro="Divisão por zero não é permitida!")
            resultado = num1 / num2

        return render_template("index.html", num1=num1, num2=num2, operacao=operacao, resultado=resultado, calculado=True)

if __name__ == "__main__":
    app.run(debug=True)