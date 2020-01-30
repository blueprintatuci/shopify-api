import requests
import shopify
from api import API
from typing import List
import mysql.connector as sql

def get_blogs() -> List[tuple]:
    """ Gets ID and Title of all blogs
    Args:
        N/A
    Returns:
        Tuple of blog info (id,title)
    """
    r = requests.get(API.BLOG_URL)
    blogs = []
    # print(r_get_blogs.status_code,r_get_blogs.json())
    for blog in r.json()['blogs']:
        blogs.append((blog['id'],blog['title']))
    
    return blogs

def get_articles() -> List[List]:
    """
    """
    pass

def post_articles(blog_id: str, data: dict):
    """
    """
    r = requests.post(API.ARTICLE_URL_post(API.ADMIN_URL,blog_id),json={'article':data})
    return r


if __name__ == '__main__':
    data = {
            "title": "API test",
            "author": "John Luong",
            "tags": "api, tag1, tag2",
            "body_html": "<h1>api test post</h1>\n<p><strong>YEET</strong></p>",
            "published_at": "Thu Mar 24 15:45:47 UTC 2011"
            }
            
    print(post_articles("53068562571",data).status_code)





