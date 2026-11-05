## Evolução do MVP — Código de barras

### Origem da melhoria

Durante a validação do MVP com a proprietária de um mercadinho de bairro, foi identificada a oportunidade de agilizar a identificação dos produtos utilizando códigos de barras.

### Solução implementada

- Inclusão de um campo de código de barras no cadastro de produtos.
- Pesquisa de produtos pelo nome ou código de barras.
- Compatibilidade com leitores USB ou Bluetooth que funcionam como teclado, permitindo inserir o código no campo de pesquisa.
- Migração do banco de dados para armazenar o código de barras.
- Teste automatizado para validar a pesquisa.

### Validação realizada

A funcionalidade foi testada no ambiente local e posteriormente no sistema publicado no Render, utilizando PostgreSQL.

O cadastro de um produto com código de barras e sua localização pela pesquisa foram concluídos com sucesso.

A suíte de 15 testes automatizados também foi aprovada no GitHub Actions.

### Resultado

A melhoria atende ao feedback da parceira e amplia a praticidade do MVP, mantendo a interface simples e acessível.

**Observação:** a integração automática com o caixa e o teste com um leitor físico permanecem como possibilidades de evolução futura.