# Mercado Imobiliário Digital (RWA) 🌐 🏡

![ASPPIBRA ESCRITURA](https://raw.githubusercontent.com/ASPPIBRA-DAO/Imagens/890ffa9bfb4c79f650c48e627aa2306299c17c4b/Jornal/ASPPIBRA-ESCRITURA.svg)

<iframe width="560" height="315" src="https://www.youtube.com/embed/6R9gf_Y8GgY?si=p9ZmhOgIHQ6haNF2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
  
</iframe>

## Índice 📑

1. [**Introdução**](#introdução)
2. [**Requisitos**](#requisitos)
3. [**Recursos Principais**](#recursos-principais)
4. [**Uso**](#uso)
5. [**Modelo**](https://github.com/ASPPIBRA-DAO/WEBINAR/tree/main/Modelo%20de%20Escritura)
6. [**Contribuições**](#contribuições)
7. [**Licença**](https://github.com/ASPPIBRA-DAO/DIGITAL_WORLD_REAL_ESTATE_MARKET/blob/a145c7c2e2a1fa311bb814ed8ed9b1819a20631d/LICENSE.md)

## Introdução 🚀

O Marketplace Imobiliário Mundo Digital visa impulsionar a inclusão digital por meio da digitalização de registros imobiliários, possibilitando transações internacionais no setor imobiliário. O processo de digitalização é semiautomatizado, permitindo que os usuários do aplicativo Mundo Digital adquiram sua versão digital do registro imobiliário.

## Requisitos 📋

Para executar o contrato inteligente, você precisa ter o seguinte:

- Uma carteira Web3 💼
- Tokens de gás para pagar as taxas de rede ⛽

<br />

> 👉 Instalar os módulos via `VENV`.

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

<br />

> 👉 Edite o arquivo `.env` utilizando o modelo `.env.sample`.

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Configurar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

<br />

> 👉 Criar o Superusuário

```bash
python manage.py createsuperuser
```

<br />

> 👉 Iniciar a aplicação

```bash
python manage.py runserver
```

Neste ponto, o aplicativo é executado em `http://127.0.0.1:8000/`.

<br />

### Requisitos para digitalização de registros imobiliários 🏡

Além dos requisitos listados na seção "Requisitos" deste README, o processo de digitalização de registros imobiliários também exige a coleta das seguintes informações e documentos:

| Categoria                        | Documento                                               | Descrição                                                                                   |
|----------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Informações pessoais:**       | Nome completo                                           | Nome completo do proprietário                                                              |
|                                  | Data de nascimento                                      | Data de nascimento do proprietário                                                          |
|                                  | CPF                                                     | Cadastro de Pessoa Física do proprietário                                                   |
|                                  | RG                                                      | Registro Geral do proprietário                                                              |
|                                  | Nacionalidade                                           | Nacionalidade do proprietário                                                               |
|                                  | Estado civil                                            | Estado civil do proprietário                                                                |
| **Comprovante de residência:**   | Conta de água                                           | Comprovante de residência referente ao fornecimento de água                                 |
|                                  | Conta de luz                                            | Comprovante de residência referente ao fornecimento de energia elétrica                     |
|                                  | Conta de gás                                            | Comprovante de residência referente ao fornecimento de gás                                  |
| **IPTU:**                        | Comprovante de pagamento do IPTU                        | Comprovante de pagamento do Imposto sobre a Propriedade Territorial Urbana                  |
| **Ônus reais:**                  | Comprovante de ônus reais                               | Documento que comprova a existência de ônus reais sobre o imóvel                            |
| **Planta topográfica do lote:** | Planta topográfica                                      | Documento que representa a forma e as dimensões do lote                                     |
| **Planta arquitetônica:**        | Planta arquitetônica do imóvel                          | Documento que representa a distribuição interna do imóvel                                   |
| **Planta de zoneamento:**        | Planta de zoneamento                                    | Documento que representa a divisão de uma área urbana em zonas específicas                  |
| **Escritura:**                   | Escritura                                               | Documento público que registra a transferência de propriedade do imóvel                     |
| **Fotos do imóvel:**             | Fotos do imóvel                                         | Fotografias do imóvel para ilustrar e facilitar a sua identificação                         |

# PRINCIPAIS CARACTERÍSTICAS

O projeto apresenta um contrato inteligente desenvolvido em linguagem Solidity, estruturado como um **mercado descentralizado para tokens não fungíveis (NFTs)**, voltado à inovação tecnológica e à transformação digital de ativos, com foco especial no setor imobiliário.

> **Nota introdutória:** O presente documento apresenta uma seleção das funcionalidades principais que estarão disponíveis na aplicação, destacando, neste momento, **aquelas diretamente integradas às tecnologias Web3 e Blockchain**. Outras funcionalidades complementares — relacionadas à gestão, interação social e serviços de apoio — serão abordadas oportunamente em materiais específicos.

Dentre os recursos já integrados ao ambiente Web3, destacam-se:

## 1. Digitalização do Registro Imobiliário em Formato de NFT

Permite aos usuários a emissão descentralizada de NFTs representativos de bens imóveis, conferindo autenticidade, rastreabilidade e segurança jurídica por meio da escrituração digital baseada em tecnologia blockchain.

## 2. Armazenamento Descentralizado de Dados via IPFS

Garante a integridade, permanência e descentralização dos arquivos vinculados aos NFTs por meio da integração com o sistema de armazenamento IPFS (InterPlanetary File System), assegurando a persistência e acessibilidade dos metadados e documentos digitais.

## 3. Compra e Venda de Ativos Digitais

Facilita transações peer-to-peer de NFTs em um ambiente seguro, transparente e auditável, promovendo negociações diretas entre as partes interessadas com garantia contratual automatizada.

## 4. Leilões Descentralizados

Implementa a funcionalidade de leilões públicos de ativos digitais, com lances registrados em tempo real na blockchain, assegurando transparência, equidade e ampla competitividade entre os participantes.

## 5. Financiamento Coletivo (Crowdfunding Imobiliário)

Habilita a captação de recursos por meio de mecanismos de financiamento coletivo, permitindo que múltiplos investidores adquiram cotas representadas por NFTs fracionados, democratizando o acesso a investimentos e impulsionando o desenvolvimento de projetos comunitários e sustentáveis.

## 6. Lojas Virtuais e Perfis Profissionais

Fornece uma infraestrutura para a criação de lojas digitais customizáveis e perfis profissionais verificados, promovendo a visibilidade institucional de agentes e empreendedores, com exibição de portfólios, credenciais e serviços oferecidos no ecossistema descentralizado.

## 7. Incubação e Lançamento de Projetos

Estabelece um ambiente favorável à incubação de iniciativas inovadoras, oferecendo suporte técnico, jurídico e operacional para o desenvolvimento e o lançamento de novos projetos dentro do ecossistema, com acesso a ferramentas de governança, financiamento e exposição mercadológica.

## Utilização 🛠️

### Screenshots

> [Mundo Digital](https://) - `Proprietários`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/d429afe0d729ceba623dba4a7437e5190a608b94/Layout_app/Escritura/Formulario01.png)
<br />

> [Mundo Digital](https://) - `Localização`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/4786522402a31fc1604dff9c72cf8a5d3926d850/Layout_app/Escritura/Localiza%C3%A7%C3%A3o.png)
<br />

> [Mundo Digital](https://) - `Prefeitura e Cartório`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/8308dbfcde8b0f09bf0694782b39b7f93322489c/Layout_app/Escritura/Prefeitura%20e%20Cartorio.png)
<br />

> [Mundo Digital](https://) - `Profissionais`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/8308dbfcde8b0f09bf0694782b39b7f93322489c/Layout_app/Escritura/Profissionais.png)
<br />

> [Mundo Digital](https://) - `Imóvel`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/4786522402a31fc1604dff9c72cf8a5d3926d850/Layout_app/Escritura/Imovel.png)
<br />

> [Mundo Digital](https://) - `Plano Arquitetônico`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/4786522402a31fc1604dff9c72cf8a5d3926d850/Layout_app/Escritura/Plano%20Arquitetonico.png)
<br />

> [Mundo Digital](https://) - `Plano Topográfico`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/4786522402a31fc1604dff9c72cf8a5d3926d850/Layout_app/Escritura/Plano%20Topografico.png)
<br />

> [Mundo Digital](https://) - `Plano de Zoneamneto`

![FORMULARIO ESCRITURA](https://github.com/ASPPIBRA-DAO/Imagens/blob/4786522402a31fc1604dff9c72cf8a5d3926d850/Layout_app/Escritura/Plano%20de%20Zoneamento.png)
<br />

<https://github.com/user-attachments/assets/e3b6e35f-e249-4605-8bdb-35fb93cba123>

<https://github.com/user-attachments/assets/e7a373a8-6e63-4f09-af9c-765f28a08c20>

# Mundo Digital (DWorld)

## Contract Tests

### Token

- [Token Contract](https://testnet.bscscan.com/token/0xb1d4a44ce8aa5e2eb2e23d7002693918f4f36c72)

### NFT

- [NFT Contract 1](https://testnet.bscscan.com/address/0x4d92829620a7dEf47Ba60f9E68eAC1e1683A87fF#code)
- [NFT Contract 2](https://testnet.bscscan.com/address/0x2cfF281E01d58143089997AC5A495D85d89D1bB2#code)

### Contracts

- [Contract 1](https://testnet.bscscan.com/address/0x3fda2E660DC06D3eCc2cC5a797af7eD8De89f2f4#code)
- [Contract 2](https://testnet.bscscan.com/address/0x7FF0884888EA59c6a02C2D8a6844A27235BA78F5#code)
- [Contract 3](https://testnet.bscscan.com/address/0x86a98eb31721f997Fed65f2aEa535DD428dCe193#code)

As a first step run the initial setup

`make setup`

Next to run the smart contract tests, in another terminal, start ganache-cli

`make ganache`

Then in the original terminal where setup was executed, run

`make test-contracts`

You can also run `make test-contracts-coverage` to see a coverage report.

## Contribuições 🤝

### Relatando Problemas 🐛

Se você encontrar algum problema ou bug, sinta-se à vontade para abrir uma issue em nosso repositório. Certifique-se de fornecer detalhes sobre o problema encontrado, incluindo etapas para reprodução, mensagens de erro e informações relevantes para facilitar a correção.

### Propondo Melhorias 🚀

Você tem ideias para melhorar o contrato inteligente ou a experiência do usuário no Marketplace Mundo Digital? Abra uma issue para discutir suas propostas. Estamos abertos a sugestões de novos recursos, melhorias de desempenho e otimizações gerais.

### Contribuindo com Código 💻

Se você deseja contribuir diretamente com o código, siga estes passos:

1. **Fork do Repositório:** Fork do nosso repositório para sua conta.
2. **Criação de Branch:** Crie uma branch para trabalhar em sua contribuição.
3. **Desenvolvimento:** Implemente suas melhorias ou correções.
4. **Testes:** Certifique-se de testar suas alterações.

5. **Pull Request (PR):** Abra um PR descrevendo suas alterações e explicando os benefícios.
6. **Revisão:** Aguarde a revisão do seu PR pelos nossos mantenedores.

### Documentação 📚

Contribuições para a documentação também são valorizadas. Se você identificar áreas que precisam de mais clareza ou quiser adicionar informações úteis, sinta-se à vontade para enviar propostas de alterações para a documentação.

Agradecemos antecipadamente seu apoio e suas contribuições para tornar o contrato inteligente do Digital World ainda melhor. Juntos, podemos criar uma plataforma mais robusta e eficiente.

## Licença 📄

Este projeto é protegido pelos termos do modelo de licença de Software Proprietário. Veja o arquivo [**Licença**](https://github.com/ASPPIBRA-DAO/DIGITAL_WORLD_REAL_ESTATE_MARKET/blob/a145c7c2e2a1fa311bb814ed8ed9b1819a20631d/LICENSE.md) para mais detalhes.
