import requests
import csv

def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print their titles
    """
    # API-dan məlumatları çək
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Status kodunu çap et
    print(f"Status Code: {response.status_code}")
    
    # Əgər sorğu uğurludursa (status code 200)
    if response.status_code == 200:
        # JSON məlumatlarını parse et
        posts = response.json()
        
        # Hər bir postun title-nı çap et
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save to CSV file
    """
    # API-dan məlumatları çək
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Əgər sorğu uğurludursa
    if response.status_code == 200:
        # JSON məlumatlarını parse et
        posts = response.json()
        
        # Data-nı strukturlaşdır - hər post üçün dictionary yarat
        structured_posts = []
        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(post_dict)
        
        # CSV faylına yaz
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Sütun başlıqlarını təyin et
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Başlıqları yaz
            writer.writeheader()
            
            # Məlumatları yaz
            for post in structured_posts:
                writer.writerow(post)
