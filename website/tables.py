from flask_table  import Table, Col 

class booking_results (Table):
    #id = Col('id', show = false)
    username = ('users')
    eventname = ('Event Name')
    ticketqty = ('Number of Tickets')
    price = ('price')

