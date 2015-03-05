#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""

        metodo = request.split(' ', 2)[0]
        recurso = request.split(' ',2)[1]
        #EL CUERPO DEL POST DEL FORMULARIO VENDRA DE LA FORMA DE campo=valor1&campo2=valor2....
        if metodo == "POST":
            cuerpo = request.split('\r\n\r\n', 1)[1]
        else:
            cuerpo = ""
        return (metodo, recurso, cuerpo)
    def process(self, (metodo, recurso, cuerpo)):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        #CONSTRUCCION DEL FORMULARIO QUE VA A IR SIEMPRE DESPUES DE LA PAGINA
        formulario = "<form method='post'>Dale un contenido:<input type='text' name='contenido' value='' /><button type='submit'>Enviar Contenido</button></form>"
        
        if metodo == "GET":
            if recurso in self.content:
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[recurso] + formulario + "</body></html>"

            else:
                httpCode = "404 Not Found"
                htmlBody = "<html><body>Not Found" + formulario + "</body></html>"
            return (httpCode, htmlBody)
        #CON POST PONGO O ACTUALIZO CONTENIDO A LA PAGINA
        elif metodo == "POST":
            contenido = cuerpo.split("=")[1]
            self.content[recurso] = contenido
            return ("200 OK", "<html><body>" + self.content[recurso] + formulario + "</body></html>")


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
