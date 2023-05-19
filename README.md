# Sobre este repositório

Este repositório faz parte um atividade do curso **Python 1: fundamentos**, do Senac São Carlos. Esta é a atividade final, da aula 09. Ela também pode ser modificada para se passada em qualquer outro curso.

__Este repositório não está completo__, ainda restam adicionar mais algumas coisas novas por aqui.

## Objetivos
- Realizar um login e cadastro de usuários
- Usar um arquivo .csv para armazenar tais usuários, simulando um banco de dados
- Ter um arquivo de CRUD com as funções básicas de operação com o banco 

## Atividades e tarefas
Certamente não é possível passar todo o conteúdo desse repositório para que os alunos possam terminar em sala de aula.

Ele pode servir como uma tarefa para que os alunos treinem seus conhecimentos e habilidades em casa para finalizar o conteúdo.

## CRUD:
- busca( nome )
- buscaTodos()
- insere( nome, senha )
- altera( nome, senha )
- remove( nome )

__Alterações__
- Invés de busca, teremos buscaNome e buscaSenha para retornar um item específico da lista

__Tarefas__
- Esse repositório tem apenas as operações de busca, buscaTodos e insere. A sugestão é que os demais comandos devem ser feito pelo próprio aluno, como uma tarefa de casa.

## Parte 1: autenticação
A primeira parte da aula será apenas para criar os arquivos e entender como eles funcionam em conjunto.

### 1. Criando os arquivos
No início da aula, criamos os arquivos:
- (bd_usuarios.csv)[./bd_usuarios.csv]: vamos usar como base para o banco de dados local simples. Nesse momento os alunos devem criar o banco e experimentar seu uso no Excel.
- (main.py)[./main.py]: arquivo principal que vamos rodar o nosso programa
- (crud.py)[./conexao.py]: responsável por criar a conexão com o banco de dados 
- (crud.py)[./crud.py]: onde vão ficar as funções de operação com o banco

### 2. Ambientar os alunos
Os alunos devem ser introduzidos ao ambiente de dicionários de forma simples. Também deve ser explicado sobre o __Pandas__ e também fazer sua instalação.

Em seguida, no arquivo _main_, vamos pedir que o usuário digite seu nome e sua senha.
Nesse momento é interessante indagar os alunos sobre como a conexão com o banco pode ser feita.

### 3. Conexão
Depois, vamos montar os arquivos de conexão e interação com o banco de dados.
Nessa etapa, vamos escrever todos os códigos do arquivo _conexao.py_ e apenas a função buscaNome e buscaSenha do _crud_.

### 4. Validação
Após montado os arquivos de conexão, os alunos devem importar o arquivo de _crud_ no _main_ e usar as funções de consulta para verificar se os dados estão realmente sendo buscados do banco.

Para concluir, os códigos escritos no _main_ podem ser transferidos para uma função.

## Parte 2: listar usuários
A opção de listagem deve chamar a função __buscaTodos__ que está no _crud_. Como o __Pandas__ já monta um dataframe formatado, não é necessário fazer nada além de printar a própria conexão.

No entanto, será preciso fazer algumas pequenas modificações no código:

### 1. Sistema cíclico
Após listar os usuários, o sistema deve voltar para o menu de opções.

O problema é que se a função que mostra opções for chamada novamente, vamos criar todo o conteúdo do _main_ dentro de uma condição. Para resolver isso, deverá ser criada uma nova variável global no _main_ chamada __usuario_autenticado__ que será verificada no começo do código do _main_.

_Se_ o usuário não estiver autenticado, ele deve cair no bloco que pede a autenticação (já está escrito), _senão_ nada acontece o código segue. Seguindo o código, o usuário irá cair direto no menu de opções invés do bloco de códigos que pede a autentiação.

Vale lembrar que será necessário acrescentar *usuario_autenticado = False* no momento que o usuário optar por sair do sistema no menu de opções.

### 2. Atualizar conexão
É necessário atualizar a variável _con_ para que ela busque o novo dataframe após inserir, alterar ou remover um usuário, pois ele ainda está carregando a conexão anterior.
__Não precisa ser dito até a parte de inserir novos usuários__

## Parte 3: inserir usuário
Caso o usuário tenha chegado a parte 2, ele está autenticado e validado e pode usar o sistema. O sistema deve dar opções do que o usuário pode fazer ou não. Uma das opções e a primeira a ser abordada, é sobre como inserir um usuário no banco.

### 1. Opções
Criar uma função que ofereça as opções do que pode ser feito no sistema. As opções são de cadastrar, alterar, alterar e sair do sistema.

### 2. Sair do sistema
Uma das opções é sair do sistema. Os alunos devem fazer um _if_ para verificar se essa opção foi escolhida. Caso o usuário decida por sair do sistema, uma mensagem deve aparecer na tela _"Você saiu do sistema"_ e retornar o usuário para início do código, chamando o _main_

### 3. Dados do novo usuário
Ainda no _main_, os alunos devem pedir os dados de cadastro do novo usuário, como nome e senha.
Nesse momento, os alunos devem ser indagados sobre como fazer esse novo cadastro. Então seguimos para a próxima etapa

### 4. Função insere
No arquivo _crud_ vamos criar a função __insere__, que pede o nome e senha do novo usuário.

A função deve ler o arquivo *bd_usuarios.csv* e gravar um novo registro ao final dele.

_Vale lembrar que os usuários podem usar o arquivo de validação de nomes da aula passada se quiserem._