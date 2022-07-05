from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class TestBlog(TestCase):

                # animes

    def test_borrar_anime__usuario_no_logueado(self):
        """
        Un usuario que no este logueado no puede borrar un post.
        El response va a retornar un status_code 302 que significa redirect. 
        En este caso Django por defecto redirecciona al login. 
        """
        response = self.client.get(reverse('anime_delete',kwargs={'pk':'1'}))
        self.assertRedirects(response, "/animes/entrar/?next=/animes/borrar/1/", status_code=302, target_status_code=200)

    def test_borrar_anime__usuario_logueado_dueño_user(self):
        """
        Si el usuario esta logueado y es el dueño del post tiene permisos de borrado.
        El response va a retornar un status_code 200 que significa éxito.
        """

        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('anime_delete',kwargs={'pk':'1'}))
        self.assertEqual(200, response.status_code)

    def test_borrar_anime__usario_logueado_no_dueño_del_blog(self):
        """
        Si el usuari esta logueado pero no es el dueño del post, no tiene permisos de borrado.
        El reponse va a retornar un status_code 403 que significa prohibido.
        """
        self.client.login(username='user_1', password='pass')
        response = self.client.get(reverse('blog_delete',kwargs={'pk':'1'}))
        self.assertEqual(403, response.status_code)


        # series

    def test_borrar_serie__usuario_no_logueado(self):
        """
        Un usuario que no este logueado no puede borrar un post.
        El response va a retornar un status_code 302 que significa redirect. 
        En este caso Django por defecto redirecciona al login. 
        """
        response = self.client.get(reverse('serie_delete',kwargs={'pk':'1'}))
        self.assertRedirects(response, "/series/entrar/?next=/series/borrar/1/", status_code=302, target_status_code=200)

    def test_borrar_serie__usuario_logueado_dueño_user(self):
        """
        Si el usuario esta logueado y es el dueño del post tiene permisos de borrado.
        El response va a retornar un status_code 200 que significa éxito.
        """

        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('serie_delete',kwargs={'pk':'1'}))
        self.assertEqual(200, response.status_code)

    def test_borrar_serie__usario_logueado_no_dueño_del_blog(self):
        """
        Si el usuari esta logueado pero no es el dueño del post, no tiene permisos de borrado.
        El reponse va a retornar un status_code 403 que significa prohibido.
        """
        self.client.login(username='user_1', password='pass')
        response = self.client.get(reverse('serie_delete',kwargs={'pk':'1'}))
        self.assertEqual(403, response.status_code)     
    
        # peliculas


    def test_borrar_pelicula__usuario_no_logueado(self):
        """
        Un usuario que no este logueado no puede borrar un post.
        El response va a retornar un status_code 302 que significa redirect. 
        En este caso Django por defecto redirecciona al login. 
        """
        response = self.client.get(reverse('pelicula_delete',kwargs={'pk':'1'}))
        self.assertRedirects(response, "/peliculas/entrar/?next=/peliculas/borrar/1/", status_code=302, target_status_code=200)

    def test_borrar_pelicula__usuario_logueado_dueño_user(self):
        """
        Si el usuario esta logueado y es el dueño del post tiene permisos de borrado.
        El response va a retornar un status_code 200 que significa éxito.
        """

        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('pelicula_delete',kwargs={'pk':'1'}))
        self.assertEqual(200, response.status_code)

    def test_borrar_pelicula__usario_logueado_no_dueño_del_blog(self):
        """
        Si el usuari esta logueado pero no es el dueño del post, no tiene permisos de borrado.
        El reponse va a retornar un status_code 403 que significa prohibido.
        """
        self.client.login(username='user_1', password='pass')
        response = self.client.get(reverse('pelicula_delete',kwargs={'pk':'1'}))
        self.assertEqual(403, response.status_code)   