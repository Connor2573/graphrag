# follow the guide here for set up: https://stackoverflow.com/questions/76106366/how-to-use-tiktoken-in-offline-mode-computer
import os

tiktoken_cache_dir = "/home/xarga/Downloads/tiktoken_cache"
os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir

# validate
assert os.path.exists(os.path.join(tiktoken_cache_dir,"9b5ad71b2ce5302211f9c61530b329a4922fc6a4"))

import tiktoken

encoding = tiktoken.get_encoding('cl100k_base')
print(encoding.encode('yes'))