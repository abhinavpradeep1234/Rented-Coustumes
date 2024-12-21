
<h3 align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

![JQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![NGINX](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)


</h3>

## Overview:



## Setting up environment

### Prerequisites

Before starting, ensure you have the following installed on your system:

- Python (preferably version 3.11.7 or above)
- Pip (Python package installer)
- Virtual environment (optional but recommended for creating isolated Python environments)

**Create a Virtual Environment**

> [!CAUTION]
> Not creating a virtual environment can lead to project instability.

Creating a virtual environment helps isolate your project dependencies from other Python projects on your system. To create a virtual environment, run the following commands in your terminal:

1. Create a virtual environment named 'venv'
   ```bash
   python -m venv venv
   ```
2. Activating the environment

- For windows
  ```bash
  venv\Scripts\activate
  ```


**Installing all the required libraries**

Now that you have a virtual environment set up, you can install Django and other libraries required within the project:

```bash
pip install -r requirements.txt
```





Then a super user has to be created

```bash
python manage.py createsuperuser
```

Then run the program in the development server

```bash
python manage.py runserver
```

