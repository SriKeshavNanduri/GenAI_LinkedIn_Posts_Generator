import json 

# ------------- special handling ----------------
# this import sys is needed in windows system to handle the emojis present in the jsons 
import sys
sys.stdout.reconfigure(encoding='utf-8')
# ------------- special handling ----------------

def process_posts(raw_file_path, processed_file_path = "data/processed_posts.json"):
    with open(raw_file_path,encoding='utf-8') as file : 
        posts = json.load(file) 
        enriched_posts = [] 
        for post in posts: 
            metadata = extract_metadata(post['text']) 
            post_with_metadata = post | metadata 
            enriched_posts.append(post_with_metadata) 
        
        for epost in enriched_posts : 
            print(epost)
            

def extract_metadata(post) : 
    return {
        "line_count" : 10 , 
        "language" : "English",
        "tags" : ['Mental Health', "Motivation"]
    }

if __name__ == "__main__":
    process_posts(raw_file_path = "data/raw_posts.json", processed_file_path = "data/processed_posts.json")