from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

def addhearts(text):
    return f"❤️ {text} ❤️"

env.filters["addhearts"] = addhearts

template = env.get_template("email.template.txt")

data = {
    "name": "Fabio",
    "products": [
        {"name": "HiPhony", "price": 999.3278},
        {"name": "MacTruquePro", "price": 2499.999},
    ],
    "special_customer": True
}

print(template.render(**data))