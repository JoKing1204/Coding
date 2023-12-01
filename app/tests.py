from django.test import SimpleTestCase


# Create your tests here.
class testFontTimes(SimpleTestCase):
    def testChoco(self):
        response = self.client.get("/warmup-2/font-times/?n=2&term=chocolate")
        self.assertContains(response, "chocho")

    def testPoo(self):
        response = self.client.get("/warmup-2/font-times/?n=3&term=Chocolate")
        self.assertContains(response, "ChoChoCho")

    def testA(self):
        response = self.client.get("/warmup-2/font-times/?n=3&term=Abc")
        self.assertContains(response, "AbcAbcAbc")


class NoTeenSum(SimpleTestCase):
    def test123(self):
        response = self.client.get("/logic-2/no-teen-sum/?X=1&Y=2&Z=3")
        self.assertContains(response, 6)

    def test12_13_5(self):
        response = self.client.get("/logic-2/no-teen-sum/?X=2&Y=13&Z=1")
        self.assertContains(response, 3)

    def test5_10_19(self):
        response = self.client.get("/logic-2/no-teen-sum/?X=2&Y=1&Z=14")
        self.assertContains(response, 3)


class XYZ(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?term=abcxyz")
        self.assertContains(response, True)

    def test_abcx0yz(self):
        response = self.client.get("/string-2/xyz-there/?term=abc.xyz")
        self.assertContains(response, False)

    def test_abcxyz2(self):
        response = self.client.get("/string-2/xyz-there/?term=xyz.abc")
        self.assertContains(response, True)


class Centered(SimpleTestCase):
    def test_123(self):
        response = self.client.get("/list-2/centered-average/?X=1&Y=2&Z=3")
        self.assertContains(response, 2)

    def test_456(self):
        response = self.client.get("/list-2/centered-average/?X=4&Y=5&Z=6")
        self.assertContains(response, 5)

    def test_789(self):
        response = self.client.get("/list-2/centered-average/?X=7&Y=8&Z=9")
        self.assertContains(response, 8)
