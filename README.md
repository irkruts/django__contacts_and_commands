#Homework

##Django. Contacts and CRUD.

Main task:
>Дополнить контакты. CRUD

All details:[HERE](https://lms.ithillel.ua/groups/62de6dfc9aec6f42f8454737/homeworks/63435bc18e760e4c3df3fbf6)

Make all actions needed for run homework from zero `make homework-i-run`

```
$ make homework-i-run
```

Delete all created artifacts from run `make homework-i-purge`

```
$ make homework-i-purge
```

Main routes:

+ **/** - _homepage_
+ **/contacts** - _Show all contacts_
+ **/contacts/edit_contact/** _Show all contacts and choose which edit_
+ **/contacts/edit_contact/<int:pk>** _Edit by id_
+ **/contacts/create_contact/** _Create new contact_
+ **/contacts/delete_contact/** _Show all contacts and choose which delete_

