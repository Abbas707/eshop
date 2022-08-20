## To setup the project in Docker

```sh
$ git clone <repo-url>
$ cd <path-to-docker-compose-file>
$ sudo docker-compose up --build -d
```

And navigate to ```http://0.0.0.1:8001/order/```.


## To run the project locally
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/Abbas707/eshop.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p python3.9 venv
$ source venv/bin/activate
```

Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:
```sh
(venv)$ cd E-SHOP
(venv)$ python manage.py runserver
```
And navigate to ```http://127.0.0.1:8000/order/```.

