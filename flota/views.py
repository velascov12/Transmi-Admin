from django.http import HttpResponse

def home(request):
    html = '''
    <html>
    <head>
        <title>flota home</title>
    </head>
    <body>
        <div>
            <a href="/flota/">home</a>
            <a href="/flota/lista">lista</a>
            <a href="/flota/crear">crear</a>
        </div>
        <h1>flota</h1>
        <div>
            <h2>gestion de flota</h2>
            <p>administra los vehículos de la flota transmi</p>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
