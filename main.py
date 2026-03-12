from logger import logger
from api_client import get_all_posts, get_post, create_post, update_post, delete_post
from utils import format_post, format_posts

def show_menu(commands):
  print("\n----------MENU----------")
  for name, data in commands.items():
    print(f"{name}: {data['description']}")
  print("------------------------")
  
def get_valid_id():
  try:
    return int(input("\nEnter ID post: "))
  except ValueError:
    logger.warning("Please enter only a number.")
    return None
    
def view_all_post():
  current_page = 1
      
  while True:
    posts = get_all_posts(page=current_page, limit=10)
        
    if not posts:
      print("\nNo more posts.")
      break
          
    logger.info("Displaying Posts:")
    print(format_posts(posts))
        
    action = input("\nNext page? (y/n): ").strip().lower()
          
    if action == "y":
      current_page += 1
    else:
      break
          
    input("\nPress Enter to continue...")
  
def view_post():
  entered_id = get_valid_id()
      
  if entered_id is None:
    return
      
  post = get_post(entered_id)
      
  if post is None:
    return
      
  logger.info("Displaying Original Post:")
  print(format_post(post))
      
  input("\nPress Enter to continue...")
  
def search_post():
  title = input("\nEnter title: ").strip().lower()
      
  if not title:
    print("\nPlease enter a title.")
    return
      
  posts = get_all_posts(page=None, limit=None)
      
  if posts is None:
    return
      
  matches = []
  result = 0
      
  for post in posts:
    result += 1
    if title in post["title"].lower():
      matches.append(post)
          
  if not matches:
    print(f"post with title '{title.title()}' not found.")
    return
      
  logger.info(f"Displaying Search result/s for '{title}'")
      
  result = 0
  count = len(matches)
  print(f"\n{count} post(s) found.")
  print("--------------------------")
          
  for match in matches:
    result += 1
    print(f"\nResult {result}:")
    print(format_post(match))
        
  input("\nPress Enter to continue...")
  
def create_a_post():
  entered_id = get_valid_id()
      
  if entered_id is None:
    return
      
  title = input("\nEnter the title: ").strip().title()
      
  if not title:
    print("\nPlease enter a title.")
    return
      
  post = create_post({
    "id": entered_id,
    "title": title
  })
      
  if post is None:
    return
      
  logger.info("Displaying Created post:")
  print(format_post(post))
      
  input("\nPress Enter to continue...")
  
def update_a_post():
  entered_id = get_valid_id()
      
  if entered_id is None:
    return
      
  try:
    new_user_id = int(input("\nEnter new user ID: "))
  except ValueError:
    logger.warning("Please enter only a number.")
    return
      
  title = input("\nEnter the Title: ").strip().title()
      
  if not title:
    print("\nPlease enter a title.")
    return
      
  post = update_post(entered_id, {
    "userId": new_user_id,
    "title": title
  })
      
  if post is None:
    return
      
  logger.info("Displaying Updated post:")
  print(format_post(post))
      
  input("\nPress Enter to continue...")
  
def delete_a_post():
  entered_id = get_valid_id()
      
  if entered_id is None:
    return
      
  confirm = input(f"\nAre you sure you want to delete post with ID: '{entered_id}' (y/n): ").strip().lower()
      
  if confirm != "y":
    print("\nDeletion cancelled!")
    return
  
  post = delete_post(entered_id)
      
  if post is None:
    return
      
  logger.info(f"Showing Post with id '{entered_id}' deleted successfully!")
      
  input("\nPress Enter to continue...")
      
def exit_program():
  print("\nBye!")
  return True
  
commands = {
  "VIEW_ALL": {
    "description": "View all post",
    "handler": view_all_post
  },
  "VIEW": {
    "description": "View post",
    "handler": view_post
  },
  "SEARCH": {
    "description": "Search post",
    "handler": search_post
  },
  "CREATE": {
    "description": "Create post",
    "handler": create_a_post
  },
  "UPDATE": {
    "description": "Update post",
    "handler": update_a_post
  },
  "DELETE": {
    "description": "Delete post",
    "handler": delete_a_post
  },
  "EXIT": {
    "description": "Exit",
    "handler": exit_program
  }
}

def main():
  while True:
    show_menu(commands)
    
    option = input("\nWhat would you like to do: ").strip().upper()
    
    if option in commands:
      result = commands[option]["handler"]()
      
      if result:
        break
      
    else:
      print("\nPlease enter a valid option.")
      continue
      
if __name__ == "__main__":
  main()