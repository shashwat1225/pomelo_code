import math
import os
import random
import re
import sys



#
# Complete the 'summarize' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING inputJSON as parameter.
#
import json
def summarize(inputJSON):
    data = json.loads(inputJSON)
    credit_limit = data['creditLimit']
    events = data['events']
    temp_pay = 0
    available_credit = credit_limit
    payable_balance = 0
    temp_transactions = []
    pending_transactions = []
    settled_transactions = []
    
    for event in events:
        if event['eventType'] == 'TXN_AUTHED':
            available_credit -= event['amount']
            pending_transactions.append(event)
            temp_transactions.append(event)
            
        elif event['eventType'] == 'TXN_AUTH_CLEARED':
            available_credit = credit_limit
            pending_transactions = [txn for txn in pending_transactions if txn['txnId'] != event['txnId']]
            
        elif event['eventType'] == 'TXN_SETTLED':
            available_credit = credit_limit - event['amount']
            settled_transactions.append(event)
            for i, j in zip(pending_transactions, settled_transactions):
                if i['txnId'] == j['txnId']:
                    j['pending'] = i['eventTime']
            payable_balance += event['amount']
            pending_transactions = [txn for txn in pending_transactions if txn['txnId'] != event['txnId']]
            
        elif event['eventType'] == 'PAYMENT_INITIATED':
            available_credit = credit_limit + event['amount']
            payable_balance += event['amount']
            pending_transactions.append(event)
            temp_transactions.append(event)
            
        elif event['eventType'] == 'PAYMENT_POSTED':
            for p in pending_transactions:
                if p['txnId'] == event['txnId']:
                    available_credit = credit_limit
                    payable_balance = 0
                    settled_transactions.append(p)
                    for s in settled_transactions:
                        if p['txnId'] == s['txnId']:
                            s['pending'] = p['eventTime']
                            s['eventTime'] += 1
                    pending_transactions.remove(p)
            
        elif event['eventType'] == 'PAYMENT_CANCELED':
            for p in pending_transactions:
                if p['txnId'] == event['txnId']:
                    payable_balance -= p['amount']
                    pending_transactions.remove(p)
            
            
            
            
    pending_transactions.sort(key = lambda x: x['eventTime'], reverse = True)
    settled_transactions.sort(key = lambda x: x['eventTime'], reverse = True)
    temp_transactions.sort(key = lambda x: x['eventTime'], reverse = True)
    settled_transactions = settled_transactions[:3]
    summary = f"Available credit: ${available_credit}\n"
    summary += f"Payable balance: ${payable_balance}\n"
    summary += "\nPending transactions:\n"
    '''for txn in pending_transactions:
        summary += f"{txn['txnId']}: ${txn['amount']} @ time {txn['eventTime']}\n"
    summary += "\nSettled transactions:\n"
    for txn in settled_transactions:
        summary += f"{txn['txnId']}: ${txn['amount']} @ time {txn['eventTime']}\n"
        
    return summary.strip()'''
    if pending_transactions:
        for txn in pending_transactions:
            
            amount_str = f"-${abs(txn['amount'])}" if txn['amount'] < 0 else f"${txn['amount']}"
            summary += f"{txn['txnId']}: {amount_str} @ time {txn['eventTime']}\n"
    summary += "\nSettled transactions:\n"
    if settled_transactions:
        
        for txn in settled_transactions:  
            finalAmount = txn.get('finalAmount', txn['amount'])
            finalAmount_str = f"-${abs(finalAmount)}" if finalAmount < 0 else f"${finalAmount}"
            summary += f"{txn['txnId']}: {finalAmount_str} @ time {txn['pending']} (finalized @ time {txn['eventTime']})\n"

    return summary.strip()
    
    
        
    
    
        
    
    
    
    # Write your code here
    

# if _name_ == '_main_':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     inputJSON = input()

#     result = summarize(inputJSON)

#     fptr.write(result + '\n')

#     fptr.close()