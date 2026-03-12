def format_post(post: dict) -> str:
  return(
    "\n--------------------\n" 
    f"Post ID : {post.get('id')}\n" 
    f"User ID : {post.get('userId')}\n"
    f"Title : {post.get('title')}\n" 
    f"Body : \n{post.get('body')}\n"
    "--------------------")
  
def format_posts(posts: list) -> str:
  return "".join(format_post(post) for post in posts)