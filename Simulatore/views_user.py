from init import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUser

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUser()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    form = FormularioUser(request.form)
    usuario = Usuarios.query.filter_by(US_EMAIL=form.email.data).first()
    if usuario:
        if form.password.data == usuario.US_PASSWORD:
            session['utente_login'] = usuario.US_EMAIL
            flash(usuario.US_NOME + ' logato con successo!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Utente o password non trovato')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['utente_login'] = None
    flash('Logout fatto con successo!')
    return redirect(url_for('index'))