#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def complex_topo_6hosts():
    setLogLevel('info')
    
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    info('*** Ajouter le contrôleur ONOS\n')
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    info('*** Ajouter les switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')

    info('*** Ajouter les hôtes pour chaque switch externe (6 par switch)\n')
    hosts = []
    for i, switch in enumerate([s1, s2, s3, s4], start=1):
        for j in range(1, 7):
            host = net.addHost(f'h{i}{j}', ip=f'10.0.{i}.{j}/24')
            net.addLink(host, switch)
            hosts.append(host)

    info('*** Connecter les switches externes aux switches d\'interconnexion\n')
    net.addLink(s1, s5)
    net.addLink(s2, s5)
    net.addLink(s3, s6)
    net.addLink(s4, s6)

    info('*** Connecter les switches d\'interconnexion entre eux\n')
    net.addLink(s5, s6)

    info('*** Démarrer le réseau\n')
    net.start()

    info('*** Tester la connectivité\n')
    net.pingAll()

    info('*** Lancer CLI Mininet\n')
    CLI(net)

    info('*** Arrêter le réseau\n')
    net.stop()

if __name__ == '__main__':
    complex_topo_6hosts()
