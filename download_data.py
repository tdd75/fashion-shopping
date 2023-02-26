import os
import urllib.request
from tqdm import tqdm

with open('./index.csv') as f:
    data = f.readlines()
    
for row in tqdm(data):
    image_file, url = row.split(',')
    output_file = f'/root/app/fashion-shopping/fashion_shopping_backend/api/management/commands/seeder/data/products/{image_file}'
    if os.path.exists(output_file):
        continue
    urllib.request.urlretrieve(url, output_file)
