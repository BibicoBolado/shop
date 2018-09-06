from django.test impor TesteCase, Client
from django.urls import reverse
#client simula o navegador


#teste para receber o status HTTP da view index
class IndexViewTesteCase(TestCase):
    def test_status_code(self):
        client = Client()
        response=client.get('/')
        self.assertEquals(response.status_code,200)
#existem varios assert, ele faz os testes