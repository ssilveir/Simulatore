from flask import render_template, request, redirect, session, flash, url_for
from init import db, app
from models import SM_CER
from helpers import FormularioCER


@app.route('/')
def index():
    Lista = SM_CER.query.order_by(SM_CER.ID_CER)
    return render_template('index.html', titulo='Simulatore CER', ListaCER = Lista);

@app.route('/NuovaCER')
def CER():
    if 'utente_login' not in session or session['utente_login'] == None:
        return redirect(url_for('login', proxima=url_for('CER')))
    form = FormularioCER()
    return render_template('NuovaCER.html', titulo = 'Nuova CER', form=form)

@app.route("/criar", methods=['POST',])
def criar():
    form = FormularioCER(request.form)
    if not form.validate_on_submit():
        return redirect( url_for('CER'))

    nome = form.nome.data
    provincia = form.provincia.data
    localita = form.localita.data
    indirizzo = form.indirizzo.data

    cer = SM_CER.query.filter_by(CR_NOME=nome).first()
    if cer:
        flash('CER già creata')
        return redirect(url_for('index'))
    
    nuova_cer = SM_CER(CR_NOME=nome, CR_PROVINCIA=provincia, CR_LOCALITA=localita, CR_INDIRIZZO=indirizzo)
    db.session.add(nuova_cer)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'utente_login' not in session or session['utente_login'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    CER = SM_CER.query.filter_by(ID_CER=id).first()
    form = FormularioCER()
    form.nome.data = CER.CR_NOME
    form.provincia.data = CER.CR_PROVINCIA
    form.localita.data = CER.CR_LOCALITA
    form.indirizzo.data = CER.CR_INDIRIZZO

    return render_template('editar.html', titulo = 'Modifica CER', ID_CER=id, form=form)

@app.route("/atualizar", methods=['POST',])
def atualizar():
    form = FormularioCER(request.form)

    if form.validate_on_submit():

        CER = SM_CER.query.filter_by(ID_CER=request.form['id']).first()
        CER.CR_NOME = form.nome.data
        CER.CR_PROVINCIA = form.provincia.data
        CER.CR_LOCALITA = form.localita.data
        CER.CR_INDIRIZZO = form.indirizzo.data


        db.session.add(CER)
        db.session.commit()

    return redirect( url_for('index') )

@app.route("/cancela/<int:id>")
def cancela(id):
    if 'utente_login' not in session or session['utente_login'] == None:
        return redirect(url_for('login'))
    
    SM_CER.query.filter_by(ID_CER=id).delete()
    db.session.commit()
    flash('CER cancelata con successo!')

    return redirect( url_for('index') )


