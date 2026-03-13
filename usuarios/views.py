from django.http import HttpResponse

def home(request):
    html = '''
    <html>
    <head>
        <title>usuarios home</title>
    </head>
    <body>
        <div>
            <a href="/usuarios/">home</a>
            <a href="/usuarios/lista">lista</a>
            <a href="/usuarios/crear">crear</a>
        </div>
        <h1>usuarios</h1>
        <div>
            <h2>panel de usuarios</h2>
            <p>gestion de usuarios del sistema transmi</p>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
