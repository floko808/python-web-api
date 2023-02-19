# carreagar os dados


dados = [
    {"nome": "Fabio", "cidade": "Diadema"},
    {"nome": "Karim", "cidade": "Dias d'Ávila"}
]



# processar
template = """\
<html>
<body>
    <ul>
        <li> Nome: {dados[nome]} </li>
        <li> Cidade: {dados[cidade]} </li>
    </ul>
</body>
</html>
"""

# renderizar

for item in dados:
    print(template.format(dados=item))

