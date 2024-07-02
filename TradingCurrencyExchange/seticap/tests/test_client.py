
import requests
import requests_mock
from django.test import TestCase
from seticap.client import SeticapClient

class SeticapClientTest(TestCase):
    def setUp(self):
        self.base_url = "https://proxy.set-icap.com" 
        self.timeout = 10 
        self.client_seticap = SeticapClient(self.base_url, self.timeout)

    def test_get_trm_success(self):
        """Verify the correct functioning of the make_request method within the SeticapClient class in your Django application"""
        
        response = self.client_seticap.get_trm()
        print(response)
        #response["data"]["trmchange"] = 
        self.assertEqual(response["status"],"success")
        self.assertTrue(isinstance(float(response["data"]["trm"].replace(",", "")), float))
        self.assertIsInstance(response["data"]["trmchange"],str)
        self.assertNotEqual(response["data"]["trmchange"], "")
        self.assertEqual(response["message"],"Estadisticas Precios")



    @requests_mock.Mocker()
    def test_get_trm_connection_error(self, mock):
        """Verify handling of ConnectionError in get_trm method."""
        endpoint = "seticap/api/estadisticas/estadisticasPrecioMercado/"
        url =f"{self.base_url}/{endpoint}"
        mock.post(url, exc=requests.exceptions.ConnectionError)

        response = self.client_seticap.get_trm()
        
        self.assertIn("Connection error occurred:", response)


    @requests_mock.Mocker()
    def test_get_trm_timeout(self,mock):
        """Verify handling of Timeout in get_trm method."""
        endpoint = "seticap/api/estadisticas/estadisticasPrecioMercado/"
        url =f"{self.base_url}/{endpoint}"
        mock.post(url, exc=requests.exceptions.Timeout)

        response = self.client_seticap.get_trm()

        self.assertIn("Timeout error occurred:", response)
