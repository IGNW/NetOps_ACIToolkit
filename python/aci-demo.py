"""
    Basic Connectivity Example
    Equivalent to connecting to ports to the same VLAN
"""
from acitoolkit import (Credentials, Session, Tenant, AppProfile, EPG, BridgeDomain, Context,
                        Endpoint, Subnet, Interface, L2Interface, Contract, FilterEntry)


def send_to_apic(tenant):
    """
    Login to APIC and push the config

    :param tenant: Tenant class instance
    :return: request response object
    """
    description = 'Basic Connectivity Example'
    creds = Credentials('apic', description)
    args = creds.get()

    # Login to APIC
    session = Session(args.url, args.login, args.password, False)
    session.login()
    resp = tenant.push_to_apic(session)
    if resp.ok:
        print('Success')
    return resp


def main():
    """
    Main execution routine

    :return: None
    """
    # Create a tenant
    tenant = Tenant('Solar_Meter')

    # Create a Context and Allow_All
    context = Context('Solar_Meter', tenant)
    context.set_allow_all()

    #Create App Profiles
    app_sme = AppProfile('Solar_Meter_East', tenant)
    app_smw = AppProfile('Solar_Meter_West', tenant)
    app_corp = AppProfile('Corporate_Network', tenant)

    # Create BridgeDomains
    bd_east = BridgeDomain('Bridge_Domain_East', tenant)
    bd_east.add_context(context)
    bd_east.set_arp_flood('no')
    bd_east.set_unicast_route('yes')
    subnet_east = Subnet('10.20.12.3', bd_east)
    subnet_east.set_addr('10.20.12.3/24')
    subnet_east.set_scope("public")
    bd_west = BridgeDomain('Bridge_Domain_West', tenant)
    bd_west.add_context(context)
    bd_west.set_arp_flood('no')
    bd_west.set_unicast_route('yes')
    subnet_west = Subnet('10.20.13.3', bd_west)
    subnet_west.set_addr('10.20.13.3/24')
    subnet_west.set_scope("public")
    bd_corp = BridgeDomain('Corporate_Bridge_Domain', tenant)
    bd_corp.add_context(context)
    bd_corp.set_arp_flood('no')
    bd_corp.set_unicast_route('yes')
    subnet_corp = Subnet('10.20.14.3', bd_corp)
    subnet_corp.set_addr('10.20.14.3/24')
    subnet_corp.set_scope("public")

    # Create an EPGs and assign to App Profiles
    epg_db_east = EPG('Database_EPG_East', app_sme)
    epg_db_east.add_bd(bd_east)
    epg_mw_east = EPG('Middleware_EPG_East', app_sme)
    epg_mw_east.add_bd(bd_east)
    epg_web_east = EPG('Webserver_EPG_East', app_sme)
    epg_web_east.add_bd(bd_east)
    epg_db_west = EPG('Database_EPG_West', app_smw)
    epg_db_west.add_bd(bd_west)
    epg_mw_west = EPG('Middleware_EPG_West', app_smw)
    epg_mw_west.add_bd(bd_west)
    epg_web_west = EPG('Webserver_EPG_West', app_smw)
    epg_web_west.add_bd(bd_west)
    epg_finance_corp = EPG('Corporate_Finance_EPG', app_corp)
    epg_finance_corp.add_bd(bd_corp)
    epg_hr_corp = EPG('Corporate_HR_EPG', app_corp)
    epg_hr_corp.add_bd(bd_corp)
    epg_sales_corp = EPG('Corporate_Sales_EPG', app_corp)
    epg_sales_corp.add_bd(bd_corp)
    epg_engineering_corp = EPG('Corporate_Engineering_EPG', app_corp)
    epg_engineering_corp.add_bd(bd_corp)
    epg_marketing_corp = EPG('Corporate_Marketing_EPG', app_corp)
    epg_marketing_corp.add_bd(bd_corp)   

    # Attach the EPGs to interfaces using VLAN as the encap
    # First - Create the physical interface objects
    if_101_61 = Interface('eth', '1', '101', '1', '61')
    if_101_62 = Interface('eth', '1', '101', '1', '62')
    if_101_63 = Interface('eth', '1', '101', '1', '63')
    if_101_64 = Interface('eth', '1', '101', '1', '64')
    if_101_65 = Interface('eth', '1', '101', '1', '65')
    if_101_66 = Interface('eth', '1', '101', '1', '66')
    if_101_67 = Interface('eth', '1', '101', '1', '67')
    if_101_68 = Interface('eth', '1', '101', '1', '68')
    if_102_61 = Interface('eth', '1', '102', '1', '61')
    if_102_62 = Interface('eth', '1', '102', '1', '62')
    if_102_63 = Interface('eth', '1', '102', '1', '63')
    if_102_64 = Interface('eth', '1', '102', '1', '64')
    if_102_65 = Interface('eth', '1', '102', '1', '65')
    if_102_66 = Interface('eth', '1', '102', '1', '66')
    if_102_67 = Interface('eth', '1', '102', '1', '67')
    if_102_68 = Interface('eth', '1', '102', '1', '68')
    if_101_71 = Interface('eth', '1', '101', '1', '71')
    if_101_72 = Interface('eth', '1', '101', '1', '72')
    if_101_73 = Interface('eth', '1', '101', '1', '73')
    if_101_74 = Interface('eth', '1', '101', '1', '74')
    if_101_75 = Interface('eth', '1', '101', '1', '75')
    if_102_71 = Interface('eth', '1', '102', '1', '71')
    if_102_72 = Interface('eth', '1', '102', '1', '72')
    if_102_73 = Interface('eth', '1', '102', '1', '73')
    if_102_74 = Interface('eth', '1', '102', '1', '74')
    if_102_75 = Interface('eth', '1', '102', '1', '75')

    # Second - Create a VLAN interfaces
    vlan161_db = L2Interface('vlan161_db', 'vlan', '161')
    vlan261_db = L2Interface('vlan261_db', 'vlan', '261')
    vlan162_web = L2Interface('vlan162_web', 'vlan', '162')
    vlan262_web = L2Interface('vlan262_web', 'vlan', '262')
    vlan163_mw = L2Interface('vlan163_web', 'vlan', '163')
    vlan263_mw = L2Interface('vlan263_web', 'vlan', '263')
    vlan64_corp = L2Interface('vlan64_corp', 'vlan', '64')
    vlan65_corp = L2Interface('vlan65_corp', 'vlan', '65')
    vlan66_corp = L2Interface('vlan66_corp', 'vlan', '66')
    vlan67_corp = L2Interface('vlan67_corp', 'vlan', '67')
    vlan68_corp = L2Interface('vlan68_corp', 'vlan', '68')

    # Third - Attach the VLANs to the physical interfaces
    vlan161_db.attach(if_101_61)
    vlan161_db.attach(if_101_62)
    vlan161_db.attach(if_101_63)
    vlan261_db.attach(if_102_61)
    vlan261_db.attach(if_102_62)
    vlan261_db.attach(if_102_63)
    vlan162_web.attach(if_101_64)
    vlan162_web.attach(if_101_65)
    vlan162_web.attach(if_101_66)
    vlan262_web.attach(if_102_64)
    vlan262_web.attach(if_102_65)
    vlan262_web.attach(if_102_66)
    vlan163_mw.attach(if_101_67)
    vlan163_mw.attach(if_101_68)
    vlan263_mw.attach(if_102_67)
    vlan263_mw.attach(if_102_68)
    vlan64_corp.attach(if_101_71)
    vlan64_corp.attach(if_102_71)
    vlan65_corp.attach(if_101_72)
    vlan65_corp.attach(if_102_72)
    vlan66_corp.attach(if_101_73)
    vlan66_corp.attach(if_102_73)
    vlan67_corp.attach(if_101_74)
    vlan67_corp.attach(if_102_74)
    vlan68_corp.attach(if_101_75)
    vlan68_corp.attach(if_102_75)

    # Forth - Attach the EPGs to the VLAN interfaces
    epg_db_east.attach(vlan161_db)
    epg_db_west.attach(vlan261_db)
    epg_web_east.attach(vlan162_web)
    epg_web_west.attach(vlan262_web)
    epg_mw_east.attach(vlan163_mw)
    epg_mw_west.attach(vlan263_mw)
    epg_finance_corp.attach(vlan64_corp)
    epg_hr_corp.attach(vlan65_corp)
    epg_sales_corp.attach(vlan66_corp)
    epg_engineering_corp.attach(vlan67_corp)
    epg_marketing_corp.attach(vlan68_corp)

    
    # Create the Endpoints
    # 3x DB East & 3x DB West
    db_east_ep1 = Endpoint(name='East_DB_Server_1', parent=epg_db_east)
    db_east_ep1.mac = '00:11:11:11:11:11'
    db_east_ep1.ip = '10.20.12.4'
    db_east_ep2 = Endpoint(name='East_DB_Server_2', parent=epg_db_east)
    db_east_ep2.mac = '00:11:11:11:12:11'
    db_east_ep2.ip = '10.20.12.5'
    db_east_ep3 = Endpoint(name='East_DB_Server_3', parent=epg_db_east)
    db_east_ep3.mac = '00:11:11:11:13:11'
    db_east_ep3.ip = '10.20.12.6'
    db_west_ep1 = Endpoint(name='West_DB_Server_1', parent=epg_db_west)
    db_west_ep1.mac = '00:11:11:12:11:11'
    db_west_ep1.ip = '10.20.13.4'
    db_west_ep2 = Endpoint(name='West_DB_Server_2', parent=epg_db_west)
    db_west_ep2.mac = '00:11:11:12:12:11'
    db_west_ep2.ip = '10.20.13.5'
    db_west_ep3 = Endpoint(name='West_DB_Server_3', parent=epg_db_west)
    db_west_ep3.mac = '00:11:11:12:13:11'
    db_west_ep3.ip = '10.20.13.6'

    # Assign it to the L2Interface
    db_east_ep1.attach(vlan161_db)
    db_east_ep2.attach(vlan161_db)
    db_east_ep3.attach(vlan161_db)
    db_west_ep1.attach(vlan261_db)
    db_west_ep2.attach(vlan261_db)
    db_west_ep3.attach(vlan261_db)

    # Create the Contract between Database and Middleware
    contract_db2mw = Contract('contract_db2mw', tenant)
    icmp_entry = FilterEntry('icmpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='ip',
                            prot='icmp',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_db2mw)
    arp_entry = FilterEntry('arpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='arp',
                            prot='unspecified',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_db2mw)
    tcp_entry = FilterEntry('tcpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='1433',
                            dToPort='1433',
                            etherT='ip',
                            prot='tcp',
                            sFromPort='1433',
                            sToPort='1433',
                            tcpRules='unspecified',
                            parent=contract_db2mw)
    udp_entry = FilterEntry('udpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='1433',
                            dToPort='1433',
                            etherT='ip',
                            prot='udp',
                            sFromPort='1433',
                            sToPort='1433',
                            tcpRules='unspecified',
                            parent=contract_db2mw)
    # Provide and consume the Contract
    epg_db_east.provide(contract_db2mw)
    epg_db_west.provide(contract_db2mw)
    epg_mw_east.consume(contract_db2mw)
    epg_mw_west.consume(contract_db2mw)

    # Create the Contract between Web and Middleware
    contract_web2mw = Contract('contract_web2mw', tenant)
    icmp_entry = FilterEntry('icmpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='ip',
                            prot='icmp',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_web2mw)
    arp_entry = FilterEntry('arpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='arp',
                            prot='unspecified',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_web2mw)
    tcp_entry = FilterEntry('tcpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='443',
                            dToPort='443',
                            etherT='ip',
                            prot='tcp',
                            sFromPort='443',
                            sToPort='443',
                            tcpRules='unspecified',
                            parent=contract_web2mw)
    udp_entry = FilterEntry('udpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='443',
                            dToPort='443',
                            etherT='ip',
                            prot='udp',
                            sFromPort='443',
                            sToPort='443',
                            tcpRules='unspecified',
                            parent=contract_web2mw)
    # Provide and consume the Contract
    epg_web_east.provide(contract_web2mw)
    epg_web_west.provide(contract_web2mw)
    epg_mw_east.consume(contract_web2mw)
    epg_mw_west.consume(contract_web2mw)

    # Create the Contract for Corporate users
    contract_corp = Contract('contract_corp', tenant)
    icmp_entry = FilterEntry('icmpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='ip',
                            prot='icmp',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_corp)
    arp_entry = FilterEntry('arpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='unspecified',
                            dToPort='unspecified',
                            etherT='arp',
                            prot='unspecified',
                            sFromPort='unspecified',
                            sToPort='unspecified',
                            tcpRules='unspecified',
                            parent=contract_corp)
    tcp_entry = FilterEntry('tcpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='443',
                            dToPort='443',
                            etherT='ip',
                            prot='tcp',
                            sFromPort='443',
                            sToPort='443',
                            tcpRules='unspecified',
                            parent=contract_corp)
    udp_entry = FilterEntry('udpentry',
                            applyToFrag='no',
                            arpOpc='unspecified',
                            dFromPort='443',
                            dToPort='443',
                            etherT='ip',
                            prot='udp',
                            sFromPort='443',
                            sToPort='443',
                            tcpRules='unspecified',
                            parent=contract_corp)
    # Provide and consume the Contract
    epg_engineering_corp.provide(contract_corp)
    epg_finance_corp.provide(contract_corp)
    epg_hr_corp.provide(contract_corp)
    epg_sales_corp.provide(contract_corp)
    epg_marketing_corp.provide(contract_corp)
    epg_web_east.consume(contract_corp)
    epg_web_west.consume(contract_corp)
    epg_mw_east.consume(contract_corp)
    epg_mw_west.consume(contract_corp)
    epg_db_east.consume(contract_corp)
    epg_db_west.consume(contract_corp)

    # Dump the necessary configuration
    print('URL: ' + str(tenant.get_url()))
    print('JSON: ' + str(tenant.get_json()))

    send_to_apic(tenant)

    # Clean up
    # tenant.mark_as_deleted()
    # send_to_apic(tenant)

if __name__ == '__main__':
    main()
