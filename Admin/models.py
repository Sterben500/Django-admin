from django.db import models

class server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    server_type = models.CharField(max_length=100)
    processor_numb = models.CharField(max_length=100)
    memory_capacity = models.CharField(max_length=100)
    storage_capacity = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class server_types(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class services (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    launch_date = models.DateField()
    memory_used = models.IntegerField()
    memory_necessary = models.IntegerField()
    launch_server = models.ForeignKey(server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class applications (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    server_type = models.ForeignKey(server_types, on_delete=models.CASCADE)
    users = models.ManyToManyField(users)

    def __str__(self):
        return self.name


