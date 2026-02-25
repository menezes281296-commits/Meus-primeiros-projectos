from flask import Flask, render_template
import math
import matplotlib.pyplot as plt
import numpy as np
import os
app = Flask(__name__)
@app.route("/")
def grafico():
    vendas=np.array([15.0,13.0,33.50,23.56,42.67,55.98,72.99])
    dias=(['segunda','terça','quarta','quinta','sexta','sábado','domingo'])
    faturamento_total=np.sum(vendas)
    media=np.mean(vendas)
    media_arredondada=math.ceil(media)
    if faturamento_total>150 and media_arredondada>15:
        texto_status="Investir"
        cor_do_site = "#2ecc71"
        msg = "O negócio está sólido. Hora de abrir uma filial!"
    elif faturamento_total<150 and media_arredondada>15:
        texto_status = "Alerta"
        cor_do_site = "#f1c40f"
        msg = "Vendas estáveis, mas volume baixo. Melhore o marketing."
    else:
        texto_status = "Perigo"
        cor_do_site = "#e74c3c"
        msg = "Cuidado! Risco de prejuízo nos próximos meses."
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.figure(figsize=(8,5))
    plt.bar(dias,vendas,color='green')
    plt.title('Vendas em uma semana')
    plt.xlabel("dias")
    plt.ylabel("vendas")
    plt.legend()
    plt.savefig('static/graficodebarras.png')
    plt.close()
    return render_template("index.html",valor_html=media_arredondada,cor=cor_do_site,status=texto_status)
if __name__=="__main__":
    app.run(debug=True)