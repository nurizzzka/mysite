from django.db import models

''''Создайте модель со следующими полями
Задача
Статус (запланировано, выполнено, отменено)'''
class TodoList(models.Model):
    task = models.CharField(max_length=100)

    TO_DO = 'to do'
    DONE = 'done'
    CANCELED = 'canceled'

    STATUSES = (
    		(TO_DO, 'to do'),
    		(DONE, 'done'),
    		(CANCELED, 'canceled'),
    	)

    status = models.CharField(max_length=10, choices=STATUSES, default=TO_DO)
  

    def __str__(self):
        return self.task


