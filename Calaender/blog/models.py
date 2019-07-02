from django.db import models

def changeMonth(str):
    map = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}
    return map[str]

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Schedule(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    content = models.TextField()

    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    
    allday = models.BooleanField()
    

    def __str__(self):
        return self.title