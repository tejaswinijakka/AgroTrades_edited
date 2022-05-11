from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    location=models.CharField(max_length = 50)
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_phone(phone):
        try:
            return Customer.objects.get(phone= phone)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(phone = self.phone):
            return True

        return False