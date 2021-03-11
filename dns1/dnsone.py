def menu_loop():
    """Menu"""
    accion = None
    while accion != 's':
        for key, value in menu.items():

            print((f'{key}) {value.__doc__}'))
        accion = input('\nOpcion: ').lower().strip()

        if accion in menu:
            menu[accion]()

def exit():
    """Exit"""
    accion = input('Are you sure? [Y/n] '.lower().strip())
    if accion == 'y':
        sys.exit(1)
    else:
        print('\n\n')
        menu_loop()


def options():
	option = None
	while option != 'x':
		if option == 'a':



def host_address():
	"""Host address info"""

def authoritative_name_server():
	"""Authoritative name server"""

def mail_destination():
	"""Mail destination"""

def mail_forwarder():
	"""Mail forwarder"""

def canonical_name_for_alias():
	"""Cannonical name for alias"""

def start_of_a_zone_of_authority():
	"""Start of a zone of authority"""

def mailbox_domain_name():
	"""Mailbox domain name"""

def mail_group_member():
	"""Mail group member"""

def mail_rename_domain_name():
	"""Mail rename domain name"""

def null_rr():
	"""Null rr"""

def well_known_service_description():
	"""Well known service description"""

def domain_name_pointer():
	"""Domain name pointer"""

def host_information():
	"""Host information"""

def mailbox_or_mail_list_information():
	"""Mailbos or mail list information"""

def mail_exchange():
	"""Mail exchange"""

def text_strings():
	"""Text strings"""

def transfer_of_an_entire_zone():
	"""Transfer of an entire zone"""

def mailbox_related_records():
	"""Mailbox related records"""

def mail_agent_rr():
	"""Mail agent rr"""

def all_records():
	"""All records"""


menu = OrderedDict([
    ('a', host_address),
    ('b', authoritative_name_server),
    ('c', mail_destination),
    ('d', mail_forwarder),
    ('e', canonical_name_for_alias),
    ('f', start_of_a_zone_of_authority),
    ('g', mailbox_domain_name),
    ('h', mail_group_member),
    ('i', mail_rename_domain_name),
    ('j', null_rr),
    ('k', well_known_service_description),
    ('l', domain_name_pointer),
    ('m', host_information),
    ('n', mailbox_or_mail_list_information),
    ('o', mail_exchange),
    ('p', text_strings),
    ('q', transfer_of_an_entire_zone),
    ('r', mailbox_related_records),
    ('s', mail_agent_rr),
    ('t', all_records)
    ('x', exit)
])