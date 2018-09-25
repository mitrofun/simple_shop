Simple shop
=====
Example of a store with a catalog and shopping car

Installation
====
```bash
git clone https://github.com/mitrofun/simple_shop.git
```

Run
====

Local develop
---

### Install requirements for backend
```bash
cd simple_shop
pip3 install -r requirements.txt
```
### Install requirements for frontend
**WARNING** to run the application locally, you must install it on 
your system `yarn` and `gulp` and after run command for download
 library for frontend
```bash
yarn install
gulp copy
```
**WARNING** By default, sqlite is used for local startup, which creates 
database file located at the root of the project,
to override this behavior, set the path of the variable in 
environment variable `DATABASE_URL`, for example sqlite. 
```bash
export DATABASE_URL='sqlite:////full/path/to/your/database/file.sqlite'
```
For more information on how to set up a database connection, 
see [here](https://github.com/kennethreitz/dj-database-url#url-schema)

### Migration
After roll migration
```bash
python3 manage.py migrate
```
or use command
```bash
make migrate
```
### Create admin
Create administrator with username `admin` and password `admin` 
```bash
python3 manage.py createdefaultuser
```
or use command
```bash
make user
```
### Run develop server
After run develop server
```bash
python3 manage.py runserver
```
### Fixtures
To demonstrate the project, it has fixtures with categories and products.
To load fixtures, use the following commands
```bash
mkdir -p media/products && cp -rf fixtures/products media
python3 manage.py loaddata fixtures/category.json
```

### Quick run
The project has a quick start script that does all the operations described above.
To run it, run the following command
```bash
./quick_start.sh
```

Run in docker
----
```bash
docker-compose up --build
```

Requirements
=====
- python 3.6+
- Django 2.1+
- see all requirements in [base.txt](https://github.com/mitrofun/simple_shop/blob/master/requirements/base.txt)


Tests
====
For run test use the following commands
```bash
pip3 install -r requirements/dev.txt
pytest
```

Contributors
====
- [mitri4](https://github.com/mitrofun)

License
=====
simple_shop is released under the MIT License. See the LICENSE file for more details.
