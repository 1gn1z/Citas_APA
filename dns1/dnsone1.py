import dns.resolver
from collections import OrderedDict
from pyfiglet import Figlet

banner = Figlet(font="standard")
banner2 = Figlet(font="graffiti")
# Imprimimos el texto que queramos como banner
print(banner.renderText('Dns-One'))
print(banner2.renderText('by 1gn1z'))


def menu_loop():
    """Menu"""
    accion = None
    while accion != 's':
        for key, value in menu.items():

            print((f'{key}) {value.__doc__}'))
        accion = input('\nOpcion: ').lower().strip()

        if accion in menu:
            menu[accion]()


def options():
    option = None
    while option != 'x':
        if option == 'a':
            host_address()
        elif option == 'b':
            authoritative_name_server()
        elif option == 'c':
            mail_destination()
        elif option == 'd':
            mail_forwarder()
        elif option == 'e':
            canonical_name_for_alias()
        elif option == 'f':
            start_of_a_zone_of_authority()
        elif option == 'g':
            mailbox_domain_name()
        elif option == 'h':
            mail_group_member()
        elif option == 'i':
            mail_rename_domain_name()
        elif option == 'j':
            null_rr()
        elif option == 'k':
            well_known_service_description()
        elif option == 'l':
            domain_name_pointer()
        elif option == 'm':
            host_information()
        elif option == 'n':
            mailbox_or_mail_list_information()
        elif option == 'o':
            mail_exchange()
        elif option == 'p':
            text_strings()
        elif option == 'q':
            transfer_of_an_entire_zone()
        elif option == 'r':
            mailbox_related_records()
        elif option == 's':
            mail_agent_rr()
        elif option == 't':
            all_records()
        elif option == 'x':
            exit_program()





def exit_program():
    """Exit"""
    accion = input('Are you sure? [Y/n] '.lower().strip())
    if accion == 'y':
        sys.exit(1)
    else:
        print('\n\n')
        menu_loop()



def host_address():
    """Host address"""

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
    """Mailbox or mail list information"""

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
    ('t', all_records),
    ('x', exit)
])