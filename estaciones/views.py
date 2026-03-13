from django.http import HttpResponse

def home(request):
    html = '''
    <html>
    <head>
        <title>estaciones home</title>
    </head>
    <body>
        <div class="nav">
            <a href="/estaciones/">home</a>
            <a href="/estaciones/lista">lista</a>
            <a href="/estaciones/crear">crear</a>
        </div>
        <h1>estaciones</h1>
        <div class="card">
            <h2>gestion de estaciones</h2>
            <p>administra las estaciones del sistema transmi</p>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
