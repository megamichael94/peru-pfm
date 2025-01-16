# pfm_peru

## Description
This project as the name describes, is a personal finance manager for peruvians, it started as a idea
to store all my vouchers on a centralized software, in the end of the year there are taxes to be paid
therefore an algorithm to auto-calculate is expected to be implemented by the end of the next fiscal 
year. 
This project is also intended to be read or reviewed by scouts or talent seekers whom would like
to review my python portfolio, so if you are feel free to contact me through LinkedIn or email.


## Getting started
1. Create virtual env with python3 venv_name
2. Activate the virtual environment `Scripts/activate` or in unix based os 
   `source bin/activate`
2. Cloning repo `https://github.com/megamichael94/peru_pfm`
3. Create a database with PostgreSQL preferebly
4. Install the requirements `pip install -r requirements.txt`
5. Creating enviroment variables (see example below)
6. Apply migrations `python manage.py migrate`
6. Create a superuser `python manage.py createsuperuse`
7. Finally run the server `python manage.py runserver`

## .env file
Create a file `.env` next to the manage.py file and add the following content
```python
SECRET_KEY=8asd7f98sdf98df9a8df7as89df7 # this site is good to create a new secret key https://djecrety.ir/
DEBUG=True
ALLOWED_HOSTS=localhost,192.168.1.111 # use your local ip
DATABASE_URL=psql://psql_user:psql_password@127.0.0.1:5432/database_name
CSRF_TRUSTED_ORIGINS=http://*.localhost:8000,http://*.127.0.0.1
```
DATABASE_URL
* psql: could be changed to a different database
* psql_user: username of the database
* psql_password: password used for the user
* 127.0.0.1: could be changed for a different ip if is not locally
* 5432: port of the database
* database_name: the database name


## Add your files, creating commits, messages and task priority order
Local standard used is T-123-ticket-or-task-description
- T for Trello as I handle new ideas or remaining work in Trello
- 123 is a test number that basically is autocreated in Trello task url (part of the description)
- Reference https://github.com/michaelmestaspaz/pfm_peru/tree/1-get-tax-rates-from-sunat-page


## Test and Deploy

- Test every feature newly created locally before creating a pull request
- Add unit tests if posible # todo: add testing libraries
- Test that the existing functionalities still work as intended so we don't 
  have regresion errors in updated functionalities

***

## External dependencies
Software versions tested or developed with:
- Python 3.10.6
- PostgreSQL 14.7

## <a name="usage">Usage</a>
1. Manage all your personal vouchers and finances through a centralized app
2. Migrations will ensure all models are created and the data needed for its 
   correct functionalities to work, for this there is migration in 
   `tax_rates`, 0002 that will scrap it's data from an government site

## Web scrapping
Even though is minimal, on the [usage](#usage) section 2, I mention the 
scrapping of a site to obtain oficial data needed to calculate the taxes to 
be paid at the end of the year, to do this I used `BeautifulSoup` and `requests`

## Support
If you are indeed using the system and have a new idea or an improvement, 
don't doubt to email me to discuss it 

## Roadmap
#### 2025 end of the  year objectives 
- add rest services to receive files from an app
- Create the frontend using Flutter

## Contributing
If you are a developer who likes the idea and would like to add a new feature, functionality or fix a feature
please contact me through any of my contact links so I can add you as a 
contributor

## Authors and acknowledgment
Thanks to @https://github.com/megamichael94/ as the creator
main contributors as code reviewer

## License
MIT License

Copyright (c) **2025 Michael Andre Mestas Paz**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Project status
On development and a personal version running :todo: add link
