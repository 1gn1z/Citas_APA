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
    """Salir del programa"""
    accion = input('Are you sure? [Y/n] '.lower().strip())
    if accion == 'y':
        sys.exit(1)
    else:
        print('\n\n')
        menu_loop()




menu = OrderedDict([
    ('a', host_address),
    ('b', authoritative_name_server ),
    ('c', mail_destination),
    ('d', mail_forwarder),
    ('e', canonical_name_for_alias ),
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