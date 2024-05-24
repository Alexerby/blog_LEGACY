
def user_info(request):
    user = request.user
    return {'user': user}


def nav_items(request):
    nav_items = [
        {
            'url': 'articles:index',
            'icon': 'core/icons/envelope_white.svg',
            'alt': 'Mail Icon',
            'text': 'Blogg'
        },
        {
            'url': 'about:about',
            'icon': 'core/icons/about.svg',
            'alt': 'About Icon',
            'text': 'Om mig'
        }
    ]
    return { 'nav_items': nav_items }

def socialmedia_icons(request):
    icons = [
        {
            'url': 'https://x.com/erby_alex',
            'icon': 'core/icons/socialmedia/x.svg',
            'alt': 'X (Previously Twitter)'
        },
        {
            'url': 'https://www.instagram.com/alexanderer_',
            'icon': 'core/icons/socialmedia/instagram.svg',
            'alt': 'Instagram'
        },
        {
            'url': 'https://www.linkedin.com/in/alexander-eriksson-bystrom/',
            'icon': 'core/icons/socialmedia/linkedin.svg',
            'alt': 'LinkedIn'
        },
    ]

    return { 'icons': icons }
