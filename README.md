# Pomelo Code

This repository unveils a Django-based backend framework, crafted for Pomelo's software engineer code assessment challenge. The task involved devising logic for six critical transaction and payment events inherent in credit card operations. This logic now underpins the backend layer I implemented. I have also added the input file that can be referred and used to test the backend's functionality. I have also intgrated sqlite3 database along with the backend which means all the settled transactions will be added in a queue in the database and shown to hte user whenever a POST request is made. One small change that I made while designing the server was, using accountId for the events since each account would have a separate credit limit. This functionality also lets the administrator set different credit limits for different accounts. Now in order to observe how the server functions, I have provided following simple steps for engineers to test the server out.

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/shashwat1225/pomelo_code.git
```


## Requirements

Create a virtual environment:

```
virtualenv your-env-name
```

Run environment:

Mac/Linux

```
source your-env-name/bin/activate
```

Windows

```
your-env-name\Scripts\activate
```

Now, this project requires django tools and libraries. You can install them using the command:

```
pip install -r requirements.txt
```

## Usage

To run the server live locally, use the command:

```
python manage.py runserver
```

## API Paths

To keep the architecture to the point, I have only added two paths which can also be observed in the file ```api/urls.py```

