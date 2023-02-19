# 1 conectar com o banco de dados sqlite3

from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()


# 2 definiar e criar a tabela

conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

# 3 - posts
posts = [
    {
        "title": "Como ganhar promocao em 10 anos",
        "content": """\
        Neste tutorial você aprenderá o que fazer para ser promovido após dez anos na firma.
        A forca fdo odio está contigo!
        """,
        "author": "Indio Zini"
    },
    {
        "title": "Como ofender minions",
        "content": """\
        Neste tutorial você aprenderá na prática como ofender um minion.
        <pre> import make_a_blog </pre>
        """,
        "author": "Jhon The Lightning"
    },
]

# 4

count = cursor.execute("select * from post;").fetchall()

if not count:
    cursor.executemany(
        """\
        insert into post (title, content, author)
        values (:title, :content, :author);
        """,
        posts,
    )
    conn.commit()

# 5 tests

posts = cursor.execute("select * from post;").fetchall()
assert len(posts) >= 2
