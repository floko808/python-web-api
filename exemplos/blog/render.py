from database import conn
from pathlib import Path
# 1 - obter os dados

cursor = conn.cursor()

fields = ("id", "title", "content", "author")

res = cursor.execute("select * from post;")

posts = [dict(zip(fields, post)) for post in res]

# 2 criar a pasta de destino do site
site_dir = Path("site")
site_dir.mkdir(exist_ok=True)

# 3 - criar uam funcao para gerar a url com slug

def get_post_url(post):
    slug = post["title"].lower().replace(" ", "-")
    return f"{slug}.html"

# 4 - renderizar index.html

index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li><a href='{get_post_url(post)}'>{post['title']}</a> </li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)

# 5 - renderizar as paginas do blog

for post in posts:
    post_template = Path("post.template.html").read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))

conn.close()