from django.http import HttpResponse

def home(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>mantenimiento home</title>
    </head>
    <body>
        <div class="nav">
            <a href="/mantenimiento/">home</a>
            <a href="/mantenimiento/lista">lista</a>
            <a href="/mantenimiento/crear">crear</a>
        </div>
        <h1>mantenimiento</h1>
        <div class="card">
            <h2>gestión de mantenimiento</h2>
            <p>control de mantenimiento de unidades</p>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
