from flask import Flask, request, render_template
import sqlite3 as sql

app = Flask(__name__)
banco = 'candidatos.db'

# Função
def abrir_con(banco):
    con = sql.connect(banco, timeout=10)
    cur = con.cursor()
    return con, cur

def fechar_con(con):
    con.commit()
    con.close()


# Comandos SQL
contagem = "SELECT COUNT(*) FROM candidatos;"
select_todos = "SELECT * FROM candidatos;"
truncate = "DELETE FROM candidatos;" #"TRUNCATE TABLE candidatos;"
group_by = "SELECT id,nome, sum(cargo) as cargo,preco FROM candidatos WHERE cargo >= 1 GROUP BY nome;"
select_id = "SELECT * FROM candidatos WHERE id like ?"
delete_id = "DELETE FROM candidatos WHERE id like ?"
select_numero = "SELECT * FROM candidatos WHERE numero like ?"
delete_nome = "DELETE FROM candidatos WHERE nome like ?"
insert = "INSERT INTO candidatos VALUES (null, :numero, :cargo, :nome)"
insert_id = "INSERT INTO candidatos VALUES (:id, :numero, :cargo, :nome)"
update = '''
UPDATE candidatos SET
    id = :id,
    cargo = :cargo
WHERE id like :id
'''
update_name = '''
UPDATE candidatos SET
    cargo = :cargo
WHERE nome like :nome
'''

# Adição de candidatos
@app.route('/add/')
#?id=1&numero=1212&cargo=Prefeito&nome=LeoMaromba
def adicionar_candidatos():
    candidato=request.args.to_dict() #{chave: valor, chave:valor,...}
    if 'id' not in candidato:
        if candidato: # se tem argumento
            con, cur = abrir_con(banco)
            cur.execute(insert, candidato)
            fechar_con(con)
            return candidato
        else: # se não tem argumento
            return {'error': 'solicitação sem argumentos!'}
    else:
        if candidato: # se tem argumento
            con, cur = abrir_con(banco)
            cur.execute(insert_id, candidato)
            fechar_con(con)
            return candidato
        else: # se não tem argumento
            return {'error': 'solicitação sem argumentos!'}

# Remoção de candidatos
@app.route('/delete_all/')
def delete_tudo():
    con, cur = abrir_con(banco)
    resultado = cur.execute(truncate).rowcount
    fechar_con(con)
    return {'message': 'todos os candidato(s) foram removido(s) do candidatos!'}
# Alteração de cargo
#?id=1&nome=banana&cargo=12
# update
@app.route('/update_id/<id>/')
def update_id(id):
    consulta = read_id(id)
    if consulta: # existe nome no banco de dados
        candidato=request.args.to_dict() #{chave: valor, chave:valor,...}
        if candidato['cargo'] != '0':
            if candidato: # se tem argumento
                con, cur = abrir_con(banco)
                cur.execute(update, candidato)
                fechar_con(con)
                return candidato
            else: # se não tem argumento
                return render_template('atualizacao.html', candidato=consulta[0],id=id)
        else:
            con, cur = abrir_con(banco)
            resultado = cur.execute(delete_id, [id]).rowcount
            fechar_con(con)
    else: # não existe no banco de dados
        return {'erro': 'candidato não encontrado!'}

@app.route('/update_nome/<nome>/')
def update_nome(nome):
    consulta = read_nome(nome)
    if consulta: # existe nome no banco de dados
        candidato=request.args.to_dict() #{chave: valor, chave:valor,...}
        if candidato: # se tem argumento
            con, cur = abrir_con(banco)
            cur.execute(update_name, candidato)
            fechar_con(con)
            return candidato
        else: # se não tem argumento
            return render_template('atualizacao.html', candidato=consulta[0],nome=nome)
    else: # não existe no banco de dados
        return {'erro': 'candidato não encontrado!'}

# Consulta de itens
# read por id
# read all
@app.route('/read/')
def read():
    con, cur = abrir_con(banco)
    resultado = cur.execute(select_todos).fetchall()
    fechar_con(con)
    return resultado

@app.route('/read_id/<id>/')
def read_id(id):
    con, cur = abrir_con(banco)
    resultado = cur.execute(select_id, [id]).fetchall()
    fechar_con(con)
    return resultado

@app.route('/read_numero/<numero>/')
def read_nome(numero):
    con, cur = abrir_con(banco)
    resultado = cur.execute(select_numero, [numero]).fetchall()
    fechar_con(con)
    return resultado



if __name__ == '__main__':
    app.run(app.run(port=8080, host='0.0.0.0', debug=True))