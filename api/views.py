from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account, Transaction, EventType
from .serializers import TransactionSerializer
from django.http import HttpResponse



@api_view(['GET'])
def get_account_details(request, account_id):
    account = Account.objects.get(pk=account_id)
    pending_transactions = Transaction.objects.filter(account=account, event_type__name='TXN_AUTHED')
    settled_transactions = Transaction.objects.filter(account=account, event_type__name='TXN_SETTLED')
    data = {
        'pending_transactions': TransactionSerializer(pending_transactions, many=True).data,
        'settled_transactions': TransactionSerializer(settled_transactions, many=True).data
    }
    return Response(data)

@api_view(['POST'])
def process_event(request):
    data = request.data
    account = Account.objects.get(pk=data['accountId'])
    temp_transactions = []
    pending_transactions = list(Transaction.objects.filter(account=account, event_type__name='TXN_AUTHED'))
    settled_transactions = list(Transaction.objects.filter(account=account, event_type__name='TXN_SETTLED'))

    for event in data['events']:
        event_type = EventType.objects.get(name=event['eventType'])
        amount_value = event.get('amount', 0)
        transaction = Transaction.objects.create(
            account=account,
            event_type=event_type,
            event_time=event['eventTime'],
            txn_id=event['txnId'],
            amount=amount_value
        )

        if event['eventType'] == 'TXN_AUTHED':
            account.available_credit -= event['amount']
            temp_transactions.append(transaction)
            pending_transactions.append(transaction)
            
        elif event['eventType'] == 'TXN_AUTH_CLEARED':
            account.available_credit = account.credit_limit
            pending_transactions = [txn for txn in pending_transactions if txn.txn_id != event['txnId']]
            
        elif event['eventType'] == 'TXN_SETTLED':
            account.available_credit = account.credit_limit - event['amount']
            settled_transactions.append(transaction)
            for i, j in zip(pending_transactions, settled_transactions):
                if i.txn_id == j.txn_id:
                    j.pending = i.event_time
            account.payable_balance += event['amount']
            pending_transactions = [txn for txn in pending_transactions if txn.txn_id != event['txnId']]
            
        elif event['eventType'] == 'PAYMENT_INITIATED':
            account.available_credit = account.credit_limit + event['amount']
            account.payable_balance += event['amount']
            temp_transactions.append(transaction)
            pending_transactions.append(transaction)
            
        elif event['eventType'] == 'PAYMENT_POSTED':
            for p in pending_transactions:
                if p.txn_id == event['txnId']:
                    account.available_credit = account.credit_limit
                    account.payable_balance = 0
                    settled_transactions.append(p)
                    for s in settled_transactions:
                        if p.txn_id == s.txn_id:
                            s.pending = p.event_time
                            s.event_time += 1
                    pending_transactions.remove(p)
            
        elif event['eventType'] == 'PAYMENT_CANCELED':
            for p in pending_transactions:
                if p.txn_id == event['txnId']:
                    account.payable_balance += p.amount
                    pending_transactions.remove(p)
        
        account.save()

    serializer_data = {
        'available_credit': account.available_credit,
        'payable_balance': account.payable_balance,
        'pending_transactions': TransactionSerializer(pending_transactions, many=True).data,
        'settled_transactions': TransactionSerializer(settled_transactions, many=True).data
    }

    return Response(serializer_data)
