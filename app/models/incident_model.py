class Static_strings:
    all_records = "SELECT * FROM {};"
    error_empty = 'No records yet!'
    error_missing = 'No such record'
    error_bad_data = 'Provide correct incident details'
    error_no_id = 'We can\'t identify you, Provide your ID'
    msg_deleted = 'Record has been deleted'
    msg_updated = 'Updated record'
    selector = 'SELECT {} FROM {} WHERE incident_id = {};'
    creator = "INSERT INTO {}(comment,created_by, location, images, videos)\
     VALUES ('{}',{},'{}','{}','{}') RETURNING incident_id;"
    updater = "UPDATE {} SET {} = '{}' WHERE incident_id = {} RETURNING incident_id;"
    deleter = "DELETE FROM {} WHERE incident_id = {} RETURNING incident_id;"