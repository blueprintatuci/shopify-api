from keys import Keys

class API:

    API_KEY = Keys.API_KEY
    PASSWORD = Keys.PASSWORD
    SHARED_SECRET = Keys.SHARED_SECRET
    API_VERSION = "2020-01"

    ADMIN_URL = "https://%s:%s@ethictest.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, API_VERSION)
    BLOG_URL = ADMIN_URL+"/blogs.json"
    ARTICLE_URL_post = lambda ADMIN_URL, blog_id: f"{ADMIN_URL}/blogs/{blog_id}/articles.json"