#!/usr/bin/env python3
import cgi # common gateway interface
form = cgi.FieldStorage()
nome = form.getvalue("nome")
mensagem = form.getvalue("mensagem")

print("Content-type:text/html\r\n\r\n")
print("<html lang='en'>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<title>Contato</title>")
print("<title>Enviado</title>")
print("</head>")
print("<body>")
print("<h1>Enviado com sucesso!</h1>")
print(f"<h2>{nome} - {mensagem}</h2>")
print("</body>")
print("</html>")