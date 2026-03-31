<h1>Sistema de venda de passagens de ônibus</h1>

<p>  O projeto é composto por 2 arquivos .py entitulados “Modelagem.py” e “Exec.py”, sendo o
primeiro um arquivo contendo a construção das classes de objetos e seus métodos, e o segundo
contendo a parte da lógica e armazenamento de informações voláteis (o projeto não aborda
permanência de memória).</p>

  O tema escolhido para o projeto, como sugerido pelo título, foi um sistema de venda de
passagens de ônibus, levando em consideração que qualquer passageiro pode entrar em qualquer
parada (salvo a última) e sair em qualquer outra parada (salvo a primeira, ou paradas que já tenham
sido feitas anteriormente). Para isso, foram criados 4 itinerários, cada um deles contido dentro de
uma instância da classe “Onibus”. Em cada uma destas instâncias também é possível observar o uso
de agregação de objetos da classe “Passageiro”, numa lista de todos os passageiros registrados nesse
itinerário.

  O conceito de herança foi utilizado entre as classes “Usuario” (menos específica, contém
apenas nome e cpf) e “Passageiro” (Mais específica, também contém os dados da passagem
comprada). Similarmente, é possível observar o uso de polimorfismo entre estas classes com a
função “consulta()”.

  Além disso, como requisitado pelo enunciado do projeto, o usuário pode excluir sua
passagem, alterar seu assento, se cadastrar e consultar seus dados. Os dados do usuário são
guardados em listas dentro do sistema. Caso este possua passagem comprada, será guardado tanto
como uma instância de “Usuario” como “Passageiro”. Caso não possua, será guardado apenas como
“Usuario”, e o sistema irá guardar seus dados (nome e CPF) até que eles sejam excluídos na área
administrativa.
