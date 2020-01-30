from keys import Keys

class API:

    API_KEY = Keys.API_KEY
    PASSWORD = Keys.PASSWORD
    SHARED_SECRET = Keys.SHARED_SECRET
    API_VERSION = "2020-01"
    STORE_NAME = "ethic-blueprint"

    ADMIN_URL = f"https://{API_KEY}:{PASSWORD}@{STORE_NAME}.myshopify.com/admin/api/{API_VERSION}"
    # BLOG_URL = ADMIN_URL+"/blogs.json"
    # ARTICLE_URL_post = lambda ADMIN_URL, blog_id: f"{ADMIN_URL}/blogs/{blog_id}/articles.json"