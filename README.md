# Sistema de Controle de Estoque — Mercadinho

Sistema web desenvolvido como projeto acadêmico do curso de **Análise e Desenvolvimento de Sistemas**, com foco nas necessidades de um pequeno mercadinho de bairro.

## Objetivo

Facilitar o controle de mercadorias por meio de uma solução simples, acessível e responsiva, permitindo que a proprietária acompanhe a quantidade de produtos disponíveis, registre movimentações e identifique itens que precisam de reposição.

## Funcionalidades

- Cadastro de produtos com nome, categoria, preço e quantidade.
- Cadastro de código de barras por produto.
- Consulta de estoque por nome ou código de barras.
- Registro de entradas e saídas de mercadorias.
- Atualização automática das quantidades após movimentações.
- Alertas de estoque baixo.
- Dashboard com indicadores gerais do estoque.
- Histórico de movimentações com filtros.
- Autenticação de usuários.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem de programação |
| Django | Framework web e regras de negócio |
| HTML e Bootstrap | Interface responsiva |
| SQLite | Banco de dados no desenvolvimento local |
| PostgreSQL | Banco de dados em produção |
| Render | Hospedagem da aplicação |
| Git e GitHub | Versionamento do código |
| GitHub Actions | Execução automatizada de testes |

## Acesso ao sistema

**Aplicação publicada:** https://mercadinho-estoque.onrender.com/

O acesso às funcionalidades é protegido por autenticação.

## Validação com a parceira

O MVP foi apresentado à proprietária de um mercadinho de bairro, que realizou testes nas funcionalidades de cadastro, consulta de estoque, dashboard e movimentações.

Durante a validação, a parceira demonstrou facilidade para utilizar as funcionalidades e destacou a utilidade dos alertas e indicadores.

Como oportunidade de melhoria, sugeriu o uso de leitores de código de barras e uma futura integração com o caixa.

## Evolução do MVP — Código de barras

A partir do feedback recebido, foi implementada a identificação de produtos por código de barras.

### Alterações realizadas

- Inclusão do campo de código de barras no cadastro.
- Pesquisa por nome ou código de barras.
- Migração do banco de dados.
- Teste automatizado para validar a pesquisa.
- Publicação e validação da melhoria no ambiente de produção.

A funcionalidade permite digitar ou inserir o código usando leitores USB ou Bluetooth que operam como teclado. A utilização com um leitor físico ainda não foi validada.

## Testes e qualidade

O projeto possui **15 testes automatizados**, executados localmente e pelo GitHub Actions.

Também foram realizados testes funcionais no ambiente publicado, incluindo cadastro de produtos, entradas, saídas, alertas de estoque baixo, histórico e pesquisa por código de barras.

## Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/pamtelles/controle-estoque-mercadinho.git
cd controle-estoque-mercadinho
```

### 2. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Defina uma `SECRET_KEY` própria para o ambiente local e habilite `DEBUG=True`.

Exemplo no PowerShell:

```powershell
$env:SECRET_KEY = "chave-local-de-desenvolvimento"
$env:DEBUG = "True"
```

### 5. Preparar o banco de dados

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ e entre com o usuário criado.

## Melhorias futuras

- Testar a utilização de um leitor físico de código de barras.
- Avaliar a integração com o sistema de caixa.
- Ampliar os relatórios e indicadores de estoque.
- Realizar novas validações de usabilidade com a parceira.

## Contexto acadêmico

Projeto desenvolvido com base em uma necessidade real,