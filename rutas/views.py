from django.http import HttpResponse

def home(request):
    html = '''
    <html>
    <head>
        <title>rutas home</title>
    </head>
    <body>
        <div>
            <a href="/rutas/">home</a>
            <a href="/rutas/lista">lista</a>
            <a href="/rutas/crear">crear</a>
        </div>
        <h1>rutas</h1>
        <div>
            <h2>gestion de rutas</h2>
            <p>administra las rutas del sistema transmi</p>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
