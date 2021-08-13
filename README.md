# classroom
This is a project for private teachers to manage their students data, create classrooms and assign tasks to them.

# Installing on a local machine
This project requires python3.8 and sqlite.

Install requirements:
`
$ cd src && pip install -r requirements.txt
`
`
$ ./manage.py migrate
$ ./manage.py createsuperuser
`
Testing:
`
# run unit tests
$ python ./manage.py test
`
# Backend Code requirements:
Obey django's style guide.
Prefer English over your native language in comments and commit messages.
KISS and DRY.
Obey [django best practices] (book "Two Scoops of Django 3.0")

![main_page](https://user-images.githubusercontent.com/52655820/128743287-9d65a7d8-b36e-408b-9a9a-a4aa781d81ba.PNG)

Authorization

![login_page](https://user-images.githubusercontent.com/52655820/128745754-a626dcee-622b-4964-b044-425c6a9a9713.PNG)

Create and view your auditories

![auditory_list](https://user-images.githubusercontent.com/52655820/128748639-9152bfaa-b0a1-4802-8815-810e50401ade.PNG)
![auditory_detail_page](https://user-images.githubusercontent.com/52655820/128748660-fe2c7d26-77d6-4c21-a3ed-6fbee7247239.PNG)

Create and assign(answer if you are student) tasks. Make tasks until deadlines.

![create_task_page](https://user-images.githubusercontent.com/52655820/128748742-333e1eed-43cb-464c-94bb-2889a7f61c78.PNG)
![Assign_page](https://user-images.githubusercontent.com/52655820/128748764-8a5b11f4-7cbf-4bf8-a508-d2b65fac9806.PNG)
![tasks_list](https://user-images.githubusercontent.com/52655820/128748921-9086a706-56c1-4f1b-bd58-2c58abfde002.PNG)

