def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    body = b"<strong>Hello Python!</strong>"
    start_response(status, headers)
    return [body]