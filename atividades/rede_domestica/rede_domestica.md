# 🔹 Atividade: Montagem de uma Rede Doméstica

## 🎯 Objetivo

Aprender como dispositivos de rede se interconectam, configurando endereçamento IP, roteamento básico e compartilhamento de recursos em um ambiente simples, mas próximo da realidade.

## 🛠️ Componentes necessários

- Roteador (pode ser físico ou simulado no Packet Tracer/GNS3).

- Switch (gerenciável ou não).

Dispositivos finais:

- 2 computadores (PCs ou notebooks).

- 1 smartphone (se for simulação, use PCs representando).

- 1 impressora em rede (opcional, pode ser simulada).

## 📌 Etapas da Atividade

1. Montagem física ou lógica

- Conecte o roteador ao switch usando um cabo de rede (porta LAN do roteador → porta do switch).

- Conecte os dispositivos finais (PCs, notebooks, impressora) ao switch.

- Se quiser, conecte também um Access Point para simular Wi-Fi (opcional).

2. Configuração de IPs

- Configure o roteador como servidor DHCP, para que ele distribua IPs automaticamente (ex.: faixa 192.168.0.0/24).

- Cada dispositivo conectado ao switch deverá receber um IP da faixa configurada.

- Teste conectividade usando o ping entre os dispositivos (ex.: PC1 → PC2, PC1 → impressora).

3. Testes de conectividade

- Acesse o roteador a partir de um PC (via navegador ou linha de comando).

- Verifique se os dispositivos conseguem acessar a internet (se houver conexão WAN).

- Se não houver internet, teste a comunicação apenas dentro da LAN.

4. Recursos extras (opcional)

- Configurar VLANs: se o switch for gerenciável, crie uma VLAN para dispositivos pessoais e outra para dispositivos de convidados.

- Compartilhar impressora: configure uma impressora na rede e teste impressão via IP.

- Controle de acesso: configure uma senha de acesso ao roteador e regras simples de firewall.

- Monitoramento: use o Wireshark em um PC para capturar pacotes e observar protocolos em ação (ARP, DHCP, ICMP, etc.).