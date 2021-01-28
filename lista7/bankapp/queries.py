def fetch_transaction_query(userid, username):
    return '''
            SELECT u_from.username, a_from.account_number, u_to.username, a_to.account_number, amount, date, message, t.id 
            FROM bankapp_transaction AS t
            LEFT JOIN auth_user AS u_from ON t.from_account_id = u_from.id
            LEFT JOIN auth_user AS u_to ON t.to_account_id = u_to.id
            LEFT JOIN bankapp_useraccount AS a_from ON t.from_account_id = a_from.id
            LEFT JOIN bankapp_useraccount AS a_to ON t.to_account_id = a_to.id
            WHERE accepted=TRUE AND (u_from.id = '%s' OR u_from.username = '%s') AND (u_to.id = '%s' OR u_to.username = '%s') ORDER BY date DESC;
        ''' % (userid, username, userid, username)
