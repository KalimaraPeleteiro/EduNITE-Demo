from pymongo import MongoClient
from flask import Flask, render_template 

app = Flask(__name__, template_folder="html")

cliente = MongoClient()
colecao = cliente.EduNITE.Cursos

@app.route("/")
def todos_cursos():
    return render_template("index.html", documentos = colecao.find())

@app.route("/curso/<string:nome_curso>")
def curso_especifico(nome_curso):
    curso = colecao.find_one({"Curso": nome_curso})
    return render_template("especifico.html", documento = curso)

app.run(debug=True)