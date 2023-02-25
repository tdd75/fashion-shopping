import os

services = {
    'fashion_shopping_admin': 'fashion-shopping-admin',
    'fashion_shopping_app': 'fashion-shopping-app',
    'fashion_shopping_backend': 'fashion-shopping-backend',
    'fashion_shopping_chatbot': 'fashion-shopping-chatbot',
    'fashion_shopping_image_search': 'fashion-shopping-image-search',
}

github_url = 'https://github.com/tdd75/'

for folder, repo in services.items():
    if not os.path.exists(folder):
        os.system(f'git clone {github_url + repo} {folder}')
    else:
        os.system(f'cd {folder} && git pull && cd ..')
