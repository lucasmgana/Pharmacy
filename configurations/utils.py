import re

def slugify(to_slug):
    to_slug = to_slug.lower().strip()
    to_slug= re.sub(r'[^\w\s-]', '', to_slug)
    to_slug= re.sub(r'[\s_-]+', '-', to_slug)
    to_slug= re.sub(r'^-+|-+$', '-', to_slug)
    return to_slug
