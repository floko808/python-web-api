function emite_alerta(text) {
    alert("Python Expert! " + text);
}

logo_python = document.getElementsByTagName("img")[0]
logo_python.onclick = emite_alerta;

logo_django = document.getElementsByTagName("img")[1]
logo_django.onclick = emite_alerta;