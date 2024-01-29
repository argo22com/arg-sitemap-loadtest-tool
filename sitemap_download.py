from usp.tree import sitemap_tree_for_homepage
import sys

# download sitemap and save to file

url = sys.argv[1] if len(sys.argv) > 1 else 'https://exampl.com/'

tree = sitemap_tree_for_homepage(url)

with open('sitemap.txt', 'w') as f:
    for sitemap in tree.all_pages():
        f.write(sitemap.url + '\n')
