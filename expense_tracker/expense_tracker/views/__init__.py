from .default import home_page


def includeme(request):
	config.add_view(home_page, route_name='home')
