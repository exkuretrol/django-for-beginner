from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    page = "home"
    msg = f"Expected HTTP 200 status code at page '{page}'"

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, self.msg)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200, self.msg)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html", self.msg)

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>home page</h1>")

class AboutpageTests(SimpleTestCase):
    page = "about"
    msg = f"Expected HTTP 200 status code at page '{page}'"

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200, self.msg)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200, self.msg)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html", self.msg)

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>about page</h1>")
