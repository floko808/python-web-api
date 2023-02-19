import click
from blog.database import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_simplelogin import SimpleLogin


def create_user(**data):
    """ creates user with encrypted password."""
    if "username" not in data or "password" not in data:
        raise ValueError("username or password are required.")
    data["password"] = generate_password_hash(
        data.pop("password")
    )
    # TODO: verificar se o usuario já existe
    mongo.db.users.insert_one(data)

    return data


def validate_user(user):
    """Validades User Login"""
    if "username" not in user or "password" not in user:
        raise ValueError("username or password are required.")
    db_user = mongo.db.users.find_one({"username": user["username"]})
    if db_user and check_password_hash(db_user['password'], user['password']):
        return True

    return False


def configure(app):
    SimpleLogin(app, login_checker=validate_user)

    @app.cli.command()
    @click.argument("username")
    @click.password_option()
    def add_user(username, password):
        """Creates a new user"""
        user = create_user(username=username, password=password)
        click.echo(f"user created: {user['username']}")


