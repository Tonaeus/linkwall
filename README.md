# Linkwall

Linkwall is a web application that lets users create a single web page to showcase all their links.

## Website

Visit the website at [https://linkwall.tonytran.dev/](https://linkwall.tonytran.dev/).

## Technology

**Database**: SQLite  
**Backend**: Django  
**Frontend**: HTML, CSS, JavaScript, Tailwind CSS  
**Deployment**: Digital Ocean, Gunicorn, Nginx, Cloudflare

## Development

1.  ```bash
    git clone https://github.com/Tonaeus/linkwall.git
    ```

2.  ```bash
    cd linkwall
    ```

3.  ```bash
    python3 -m venv venv
    ```

4.  ```bash
    source venv/bin/activate
    ```

5.  ```bash
    pip3 install -r requirements.txt
    ```

6.  ```bash
    vim .env
    ```

7.  ```bash
    python3 manage.py makemigrations
    ```

8.  ```bash
    python3 manage.py migrate
    ```

9.  ```bash
    python3 manage.py createsuperuser
    ```

10. ```bash
    python3 manage.py runserver
    ```

11. ```bash
    deactivate
    ```

12. ```bash
    cd ..
    ```

## Contact

For questions or issues, please open an issue on GitHub or contact me at [tonytran.tt890@gmail.com](mailto:tonytran.tt890@gmail.com).
