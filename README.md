# Pomelo Code

This repository provides a django based backend architecture of the problem that we were supposed to solve for Pomelo's software engineer code assessment. In the assessment we had to create a logic for 6 transaction and payment based events that are present in any credit card's functionality. I used the same logic and applied a layer of backend on top of it. I have also added the input file that can be referred and used to test the backend's functionality. I have also intgrated sqlite3 database along with the backend which means all the settled transactions will be added in a queue in the database and shown to hte user whenever a POST request is made. One small change that I made while designing the server was, using accountId for the events since each account would have a separate credit limit. This functionality also lets the administrator set different credit limits for different accounts. Now in order to observe how the server functions, I have provided following simple steps for engineers to test the server out.

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/shashwat1225/pomelo_code.git
```


## Requirements

This project requires django tools and libraries. You can install them using the command:

```
pip install -r requirements.txt
```

## Usage

To run the server live locally, use the command:

```
python manage.py runserver
```
