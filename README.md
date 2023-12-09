# hack_hackathon_django

Simple boilerplate to set up quick projects. Useful for MVPs and hackathons.


## How to use this project

Please use the following commands for running the project and get up and running in less than 5 mins.

1. Make sure you have Python installed from version >=3.7

2. Clone this repo and navigate to the root of this project directory
    ```
    cd /path/to/hack_hackathon_django
    ```
3. Setup virtual environment and activate it
    ```
    python3 -m venv venv/
    ```
    ```
    source venv/bin/activate
    ```

4. Install dependecies
    ```
    pip install -r requirements.txt
    ```

5. Run migrations. This will create a local SQLite DB named `demo_app.sqlite`. You can change the name of your DB from `hack_hackathon_django/settings.py.`
    ```
    python3 manage.py migrate
    ```

6. Run the server. Open the browser and access your demo app at `localhost:{PORT_NUM}`
    ```
    python3 manage.py runserver {PORT_NUM}
    ```
