print("Criar VLAN em massa - Nokia")
vlan_inicio = int(input("Informe a primeira VLAN do Range: "))
vlan_final = int (input("Informe a última VLAN do Range: "))
card = int(input("Informe o card: "))
interface = int(input("Informe a interface UPLINK: "))

vlan = vlan_inicio
pon = 1

while vlan <= vlan_final:
    with open(f'CARD-{card}.txt', "a") as arquivo:
        arquivo.write(f'configure service vpls {vlan} customer 1 v-vpls vlan {vlan}\n')
        arquivo.write(f'description SLOT{card}-PON{pon}\n')
        arquivo.write(f'sap nt-a:xfp:{interface}:{vlan}\n')
        arquivo.write("exit\n")
        arquivo.write(f'sap lt:1/1/{card}:{vlan}\n')
        arquivo.write("exit\n")
        arquivo.write("no shutdown\n")
        arquivo.write("exit all\n")
        arquivo.write(f'configure vlan id {vlan} mode residential-bridge name SLOT{card}-PON{pon} in-qos-prof-name name:HSI ipv6-mcast-ctrl')
    vlan = vlan + 1
    pon = pon + 1
    
    


