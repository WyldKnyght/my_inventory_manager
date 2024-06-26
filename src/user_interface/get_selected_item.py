
def get_selected_item(listbox):
    selected = listbox.selection()
    if not selected:
        return None
    item = listbox.item(selected[0])
    return item['values']