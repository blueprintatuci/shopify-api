import requests
import shopify
from api import API
from typing import List
import mysql.connector as sql

def get_blogs() -> dict:
    """ Gets ID and Title of all blogs
    Args:
        N/A
    Returns:
        (dict) of blog info {title:id}
    """
    r = requests.get(API.BLOG_URL)
    print(r.status_code)
    blogs = {}
    # print(r_get_blogs.status_code,r_get_blogs.json())
    for blog in r.json()['blogs']:
        blogs['title'] = blog['id']
    
    return blogs

def get_blog_id_by_title(title: str) -> int:
    """ Gets blog ID given a title
    Args:
        title (str): title of blog to get
    Returns:
        (int) the ID of the blog
    """
    return get_blogs().

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
    # data = {
    #         "title": "API test",
    #         "author": "John Luong",
    #         "tags": "api, tag1, tag2",
    #         "body_html": "<h1>api test post</h1>\n<p><strong>YEET</strong></p>",
    #         "published_at": "Thu Mar 24 15:45:47 UTC 2011"
    #         }
    # blog_id = ""
            
    # print(post_articles(blog_id,data).status_code)
    print(get_blogs())




