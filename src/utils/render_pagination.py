from flask import url_for
from jinja2 import Template

def render_pagination(items, base_url):
    # Assuming `items` is a paginated object with `.pages` and `.page` attributes, like Flask-SQLAlchemy's Pagination object
    # Calculate total pages and current page
    total_pages = items.pages
    current_page = items.page

    # Generate pagination links
    pagination_links = []
    for page_num in range(1, total_pages + 1):
        url = url_for(base_url, page=page_num)
        pagination_links.append({'url': url, 'label': str(page_num)})

    # Render pagination links as HTML
    template = Template("""
        <nav aria-label="Page navigation example">
            <ul class="pagination">
                {% for link in pagination_links %}
                    <li class="page-item {% if loop.index == loop.first and loop.index == current_page %}active{% endif %}">
                        <a class="page-link" href="{{ link.url }}">{{ link.label }}</a>
                    </li>
                {% endfor %}
            </ul>
        </nav>
    """)
    return template.render(pagination_links=pagination_links, current_page=current_page)