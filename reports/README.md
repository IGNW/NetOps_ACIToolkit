#ACI Toolkit Demo Script - for ACI Always on Sandbox 

##Show Status
cd to reports directory

##Show Tenants:
python3 aci-report-logical.py -u https://sandboxapicdc.cisco.com -l admin -p ciscopsdt

##Show All:
python3 aci-report-logical.py -all -u https://sandboxapicdc.cisco.com -l admin -p ciscopsdt

##Show Security Groups:
python3 aci-report-security-audit.py -u https://sandboxapicdc.cisco.com -l admin -p ciscopsdt


##Show Report:
python3 aci-report-switch.py -u https://sandboxapicdc.cisco.com -l admin -p ciscopsdt

##GUI Version:
python3 aciREportGui.py


#Config APIC
cd to cli directory

##Show current setup:
python3 acitoolkitcli.py -l admin -p ciscopsdt -u https://sandboxapicdc.cisco.com -t show_cli.txt

##Config APIC:
python3 acitoolkitcli.py -l admin -p ciscopsdt -u https://sandboxapicdc.cisco.com -t config_cli.txt

##Reshow Conifg:
python3 acitoolkitcli.py -l admin -p ciscopsdt -u https://sandboxapicdc.cisco.com -t show_cli.txt

##Return to Reports and show them again

##Return to CLI and undo configs
python3 acitoolkitcli.py -l admin -p ciscopsdt -u https://sandboxapicdc.cisco.com -t undo_cli.txt
