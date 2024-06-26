# src/database/db_delete_elements.py
from utils.create_app import bp
from database.db_utils import delete_item

@bp.route('/admin/items/delete/<int:item_id>', methods=['POST'])
def delete_item_route(item_id):
    return delete_item(item_id)
