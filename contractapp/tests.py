""" test cases"""
#!/usr/bin/env python
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from contractapp.models import Tenant


class TenantTestCase(TestCase):
    """clss test """
    def setUp(self):
        # Tenant.objects.create(TenantName="ssi")
        # Tenant.objects.create(TenantName="mbbr")
        # self.user = User.objects.create(
        #     username
        #     email="ravi@brio.co.in",
        #     password="brio12345"
        # )
        # print(self.user)
        User.objects.create_superuser('ravi', 'ravi@brio.co.in', 'brio12345')

    def test_animals_can_speak(self):
        """nothing"""
        import pdb
        # pdb.set_trace()
        url = reverse("login")
        data = {"inputEmail": "ravi@brio.co.in", "inputPassword" :  "brio12345"}
        response = self.client.post(url, data=data)
        response = self.client.post(url, data)
        print(response)
        # ssi = Tenant.objects.get(TenantName="ssi")
        # mbbr = Tenant.objects.get(TenantName="mbbr")
        # print ssi.TenantName
        # print mbbr.TenantName

# class Testlogin(TestCase):
#     """test setup"""
#     def setUp(self):
#         import pdb
#         pdb.set_trace()
#         self.user = User.objects.create(
#             email="ravi@brio.co.in",
#             password="brio12345"
#         )
#         print(self.user)
#         User.objects.create_superuser('ravi', 'ravi@brio.co.in', 'brio12345')
#     def logintest(self):
#         """login test """
#         import pdb
#         pdb.set_trace()
#         url = reverse("login")
#         data = {"email": self.user.email, "password" :  self.user.password}
#         self.user.is_active = False
#         self.user.save()
#         response = self.client.post(url, data)
#         self.assertTrue(response.json().get("error"))
#         self.user.is_active = True
#         self.user.is_trash = True
#         self.user.save()
#         response = self.client.post(url, data)
#         self.assertTrue(response.json().get("error"))
#         data.update({"password": "invalid"})
#         response = self.client.post(url, data)
#         self.assertTrue(response.json().get("error"))
#         response = self.client.get(url, data)
#         self.assertTrue(response)
#         self.user.is_trash = False
#         self.user.save()
#         data.update({"password": self.password})
#         response = self.client.post(url, data)
#         self.assertFalse(response.json().get("error"))
#         response = self.client.post(url, data)
#         self.assertRedirects(response, reverse("hr:leave_account"), status_code=302)
#         self.user.is_superuser = True
#         self.user.save()
#         response = self.client.post(url, data)
#         self.assertRedirects(response, reverse("hr:leave_account"), status_code=302)

# import unittest

# class TestUM(unittest.TestCase):

#     def setUp(self):
#         pass

#     def test_numbers_3_4(self):
#         self.assertEqual( multiply(3,4), 12)

#     def test_strings_a_3(self):
#         self.assertEqual( multiply('a',3), 'aaa')

# def multiply(v1,v2):
#     return v1*v2

# if __name__ == '__main__':
#     unittest.main()


