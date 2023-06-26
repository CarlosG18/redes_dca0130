# Algoritmo de roteamento: OSPF

# OSPF (Open Shortest Path First)

O Protocolo de Roteamento OSPF (Open Shortest Path First) é um algoritmo amplamente utilizado para determinar as rotas mais eficientes em redes IP.

O OSPF é um protocolo de estado de enlace, o que significa que os roteadores trocam informações entre si para construir um mapa detalhado da topologia da rede. Essas informações incluem o estado dos enlaces, largura de banda, atraso e outras métricas relevantes para o roteamento.

Os roteadores OSPF dividem a rede em áreas lógicas, cada uma delas com um roteador de borda designado para lidar com a comunicação entre as áreas. Dentro de cada área, os roteadores trocam pacotes de estado de enlace para construir uma base de dados do link-state (LSDB), que contém informações sobre todos os roteadores e enlaces dentro da área.

Com base na LSDB, cada roteador OSPF calcula a árvore de menor caminho usando o algoritmo Dijkstra. Essa árvore determina as rotas mais curtas para todos os destinos possíveis dentro da área. As informações de roteamento são armazenadas em tabelas de roteamento, que são usadas para encaminhar pacotes de maneira eficiente.

Uma característica importante do OSPF é sua capacidade de lidar com atualizações de topologia de forma rápida e eficiente. Quando ocorrem mudanças na rede, como a falha de um enlace ou a adição de um novo roteador, apenas as informações afetadas são atualizadas e propagadas pelos roteadores OSPF. Isso reduz a sobrecarga de comunicação e melhora o tempo de convergência do roteamento.

**texto gerado pelo CHATGPT**


## Prática

a pratica realizada foi constituida na configuração do seguinte cenário:

![cenário de rede](https://github.com/CarlosG18/redes_dca0130/blob/main/roteamento/imgs/cenario.png)

## projeto do espaço de endereçamento

a partir deste cenário foi designado as seguintes faixas de ip:

- A rede da CASA utiliza endereçamento IPv4 na faixa 98.16.0.0/28;
- A rede da CASA com o PROVEDOR utiliza endereçamento IPv4 na faixa 119.1.0.16/30;
- A rede do PROVEDOR com a INTERNET utiliza endereçamento IPv4 na faixa 119.1.0.20/30;
- A rede da INTERNET utiliza endereçamento IPv4 na faixa 221.0.0.0/25.

podemos obter os endereços de uma forma rapida ou mais detalhada:

**Rápida**
exemplo dos ip's da rede da casa:
> como a mascara é /28 temos que o numero de bits "variaveis" é de 32-28=4. com isso temos 2⁴ = 16 endereços possiveis para esta rede. para isso basta modificar o ultimo octeto de bites do ip da rede fornecido, então teremos **endereço de rede**: `98.16.0.0` e o de **broadcast**:`98.16.0.15`.

**forma detalhada**
exemplo dos ip's da rede da internet:
> representamos o valor do ip de rede em binário: ip: 221.0.0.0 = 11011101.00000000.00000000.00000000. como a mascara indicada é /25, temos que os 25 primeiros bits são fixos e os restantes variaveis: **11011101.00000000.00000000.0**0000000. para obtermos os endereços de rede basta zerar todos os bits restantes, temos: 11011101.00000000.00000000.00000000 que transformando em decimal = 221.0.0.0. para o ultimo endereço ip temos que colocar 1 nos bits restantes desta forma: **11011101.00000000.00000000.0**1111111 que transformando em decimal temos = 221.0.0.127.


para obtermos as mascaras basta na forma como por exemplo a mascara /30, basta completamos com 30 bits com o valor igual a 1 e os restantes que no caso é 2 completamos com zeros. ao obter o valor decimal do numero binario temos a mascara correspondente:

> /30 : 11111111.11111111.11111111.11111100 = 255.255.255.252


após os calculos dos ip's foram obtidos as seguintes faixas:

| | CASA | CASA-PROVEDOR | PROVEDOR-INTERNET | INTERNET |
|:---:|:---:|:---:|:---:|:---:|
| faixa de endereços IP|rede: 98.16.0.0 - broadcast: 98.16.0.15 |rede: 119.1.0.16 - broadcast: 119.1.0.19|rede: 119.1.0.20 - broadcast: 119.1.0.23 |rede: 221.0.0.0 - broadcast: 221.0.0.127 |
| Máscara de Rede|255.255.255.240|255.255.255.252 |255.255.255.252|255.255.255.128 |
| Endereço IP do gateway| | | | |
