
def boating_nav_items(request):
    nav_items = [
        {
            'url': 'boating:boats-for-sale',
            'text': 'Till salu'
        },
        {
            'url': 'boating:boats-for-sale', # Change this
            'text': 'Uthyrning'
        },
    ]
    return { 'boating_nav_items': nav_items }
