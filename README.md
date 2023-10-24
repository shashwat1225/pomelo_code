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

This project requires django tools and libraries. You can install them using the command:

```
pip install -r requirements.txt
```

## Usage

To run the server live locally, use the command:

```
python manage.py runserver
```

After running the above command, the server will be live locally on ```http://127.0.0.1:8000/```

## API Paths

To keep the architecture to the point, I have only added two paths which would perform the transactional process, and show the settled transactions of the account.

To access that functionality, once the server is live, go on the link:
```http://127.0.0.1:8000/api/process```

To enter the transactions, you can go to the input.json file and copy one of the test cases or create test cases of your own to see how the api works. You can also use POSTMAN and send a POST request through there to see the output. 


To access the account details, after performing the process (since the database would now be populated), go on the link:
```http://127.0.0.1:8000/api/account/<int:account_id>/```

Now, in order to set a credit limit, the method is slightly tricky and technical. (Since we want only administrator to be responsible for this and with great power comes great responsibility)

If you liked my work so far, I would love to talk in detail about how I could set the credit limit, add more functionalities, make it secure (no scams, thnx), and more requests to make it async with the frontend. 

I hope you enjoy going through this as much as I enjoyed designing this. Would be highly looking forward to working with your team.

