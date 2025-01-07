import os
import sys

# Set the default cache directory
default_tiktoken_cache_dir = "C:/Users/parkc1/Documents/weird_stuff/tiktoken_cache"

# Use the environment variable if it is set, otherwise use the default
tiktoken_cache_dir = os.getenv("TIKTOKEN_CACHE_DIR", default_tiktoken_cache_dir)

os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir

# Normalize the path
tiktoken_cache_dir = os.path.normpath(tiktoken_cache_dir)

# Validate
try:
    cache_file_path = os.path.join(tiktoken_cache_dir, "9b5ad71b2ce5302211f9c61530b329a4922fc6a4")
    assert os.path.exists(cache_file_path)
except AssertionError as e:
    print(f"AssertionError: {e}")
    print("Current cache directory: ", tiktoken_cache_dir)
    # print("Error: Please follow these instructions for local-graphrag: https://github.com/battelle-software/graphrag-local")
    sys.exit(1)
except PermissionError as e:
    print(f"PermissionError: {e}")
    print("Current cache directory: ", tiktoken_cache_dir)
    print("Error: Please check the file permissions and try again.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    print("Current cache directory: ", tiktoken_cache_dir)
    sys.exit(1)