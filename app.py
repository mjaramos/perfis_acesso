#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from sistema_perfis_acesso import SistemaPerfilAcesso

app = Flask(__name__)
sistema = SistemaPerfilAcesso()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/perfis')
def api_perfis():
    return jsonify(sistema.listar_perfis())

@app.route('/api/blocos')
def api_blocos():
    return jsonify(sistema.listar_blocos())


@app.route('/api/abrangencias')
def api_abrangencias():
    return jsonify(sistema.listar_abrangencias())


@app.route('/api/consultar')
def api_consultar():
    perfil = request.args.get('perfil', '')
    abrangencia = request.args.get('abrangencia', '')
    return jsonify(sistema.consultar_funcionalidades(perfil, abrangencia))

@app.route('/api/consultarBlocos')
def api_consultarBlocos():
    bloco = request.args.get('bloco', '')
    return jsonify(sistema.consultar_bloco(bloco))


@app.route('/api/perfil', methods=['POST'])
def api_adicionar_perfil():
    nome = request.json.get('nome', '')
    return jsonify(sistema.adicionar_perfil(nome))


@app.route('/api/perfil', methods=['DELETE'])
def api_remover_perfil():
    nome = request.json.get('nome', '')
    return jsonify(sistema.remover_perfil(nome))


@app.route('/api/abrangencia', methods=['POST'])
def api_adicionar_abrangencia():
    nome = request.json.get('nome', '')
    return jsonify(sistema.adicionar_abrangencia(nome))


@app.route('/api/funcionalidade', methods=['POST'])
def api_adicionar_funcionalidade():
    d = request.json
    return jsonify(sistema.adicionar_funcionalidade(
        d.get('perfil', ''), d.get('abrangencia', ''), d.get('funcionalidade', '')
    ))


@app.route('/api/funcionalidade', methods=['DELETE'])
def api_remover_funcionalidade():
    d = request.json
    return jsonify(sistema.remover_funcionalidade(
        d.get('perfil', ''), d.get('abrangencia', ''), d.get('funcionalidade', '')
    ))


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
