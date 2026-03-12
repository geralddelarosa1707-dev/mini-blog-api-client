import requests
from config import BASE_URL as url
from logger import logger

def handle_excepts(error):
  if isinstance(error, requests.HTTPError):
    logger.error(f"Bad response from server: {error}")
      
  elif isinstance(error, requests.Timeout):
    logger.error("The request timed out.")
    
  elif isinstance(error, requests.ConnectionError):
    logger.error("\nConnection failed.")
    
  elif isinstance(error, requests.RequestException):
    logger.error(f"\nNetwork error: {error}")
  
  return None

def get_all_posts(page, limit, timeout=10):
  try:
    params = {
      "_page": page,
      "_limit": limit
    }
    response = requests.get(f"{url}/posts", params=params, timeout=timeout)
    response.raise_for_status()
    
  except requests.RequestException as error:
    return handle_excepts(error)
    
  else:
    return response.json()
  
def get_post(post_id, timeout=10):
  try:
    response = requests.get(f"{url}/posts/{post_id}", timeout=timeout)
    response.raise_for_status()
    
  except requests.RequestException as error:
    return handle_excepts(error)
    
  else:
    return response.json()
  
def create_post(data, timeout=10):
  try:
    response = requests.post(f"{url}/posts", json=data, timeout=timeout)
    response.raise_for_status()
    
  except requests.RequestException as error:
    return handle_excepts(error)
    
  else:
    return response.json()
  
def update_post(post_id, data, timeout=10):
  try:
    response = requests.patch(f"{url}/posts/{post_id}", json=data, timeout=timeout)
    response.raise_for_status()
    
  except requests.RequestException as error:
    return handle_excepts(error)
    
  else:
    return response.json()
  
def delete_post(post_id, timeout=10):
  try:
    response = requests.delete(f"{url}/posts/{post_id}", timeout=timeout)
    response.raise_for_status()
    
  except requests.RequestException as error:
    return handle_excepts(error)
    
  else:
    return response.json()