from usp.tree import sitemap_tree_for_homepage
import sys

# load and validate arguments
url = sys.argv[1] if len(sys.argv) > 1 else None

if not url or not url.startswith('http'):
    print('ERR: Provide a valid url')
    print('Example: python sitemap_download.py https://www.example.com')
    sys.exit(1)


# download sitemap and save to file
tree = sitemap_tree_for_homepage(url)
urls = [page.url for page in tree.all_pages()]

with open('sitemap.txt', 'w') as f:
    f.write('\n'.join(urls))
    print(f'File sitemap.txt created with {len(urls)} urls')
