
#  DIO - Desafio de Projeto - Criando um Sistema Bancário 🏦
Objetivo: Criar um sistema bancário que execute as operações de depósito, saque e extrato

### 🎯 Descrição do Desafio 
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar as suas operações e para isso escolheu a linguagem de programação Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: Saque, Depósito e Extrato.

💻 [BOOTCAMP DIO - Criando um Sistema Bancário com Python](https://web.dio.me/project/desafio-de-projeto-criando-um-sistema-bancario/learning/fa812356-0da6-4a85-9ffb-8b255748a288?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined)
### Especificações do Projeto

    - As operações devem ser separadas por funções: Saque, Depósito, Extrato, Cadastrar Usuário (Cliente) e Cadsatrar Conta Bancária (Vincular com usuário).

    - As funções devem ser criadas para todas as operações do sistema. Cada função terá uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida a critério do programador.


    1. Operação de Depósito

       - A função depósito deve receber os argumentos apenas por posição (positional only);

       - Não é possível realizar depósitos negativos


    2. Operação de Saque

        - A função Saque deve receber os argumentos apenas por nome (keyword only);

        - O sistema permite realizar 3 saques diários;
        - O limite máximo de cada saque é de R$500,00;
        Todos os saques devem ser demonstrados no extrato bancário


    3. Operação de Visualizar o Extrato 

        - A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

        - Essa operação deve demonstrar todos os saques e depósitos efetuados;
        - Ao final, deve ser exibido o saldo atual da contratados;
        - Os valores devem ser exibidos no formato R$ XXXX,XX
    

    4. Operação Criar Usuário (Cliente)

        - O programa deve armazenar os usuários em uma lista;

        - Um usuário é composto por: nome, data de nascimento, cpf e endereço;

        - O endereço é uma string com formato: logradouro, nro - bairro - cidade/sigla estado;

        - Deve ser armazenado somente os números do CPF;

        - Não podemos cadastrar 2 usuários com o mesmo CPF
    

    5. Cadastrar Conta Corrente

        - O programa deve armazenar contas em uma lista;

        - Uma conta é composto por agência, número da conta e usuário;

        - O número da conta é sequencial, iniciando em 1;

        - O número da agëncia é fixo: '0001';

        - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.