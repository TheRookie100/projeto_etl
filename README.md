# Criação de um Projeto de Crawler usando Scrapy e Orquestração com Dagster

<img src="/img/projeto_etl_1.png">


<p>Nesse projeto, utilizando Scrapy para a extração e Dagster para a orquestração, foram implementados dois crawlers. O primeiro é responsável por extrair as últimas notícias de um site de economia, enquanto o segundo coleta várias notícias de diferentes sites de notícias. Foi criado um pipeline que orquestra ambos os crawlers e, em seguida, armazena os dados resultantes em um arquivo JSON.

Neste tutorial, vamos aprender a criar um projeto de crawler utilizando a biblioteca Scrapy em Python e como orquestrar esse projeto com a ajuda da estrutura de orquestração Dagster.</p>

## Instalação e Configuração do Ambiente

<p>
Siga os passos a seguir para configurar seu ambiente e instalar as dependências necessárias.

1. Crie e ative um ambiente virtual:
   ```bash
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
Atualize o pip para a versão mais recente:</p>

<p>
bash
Copy code
python.exe -m pip install --upgrade pip
Instale as dependências básicas do projeto:</p>

<p>
bash
Copy code
pip install scrapy
Crie um novo projeto Scrapy:</p>

<p>
bash
Copy code
scrapy startproject <nome_do_projeto>
Crie um novo spider no projeto:</p>

<p>
bash
Copy code
scrapy genspider <nome_do_spider> <url_do_site>
Abra o arquivo do spider criado e adicione o código para extrair dados:</p>

<p>
Use XPath ou CSS selectors para selecionar os elementos HTML.
Adicione código para extrair e estruturar os dados.
Adicione o código para salvar os dados em um arquivo JSON:</p>

<p>
Você pode usar a biblioteca Scrapy ou a biblioteca built-in do Python.
Execute o spider para verificar a extração dos dados:</p>

<p>
bash
Copy code
scrapy crawl <nome_do_spider> -o <nome_do_arquivo>.json
Orquestração com Dagster
Siga os passos abaixo para criar um pipeline de orquestração usando o Dagster.</p>

<p>
Instale as dependências do Dagster e outras bibliotecas necessárias:</p>

<p>
bash
Copy code
pip install dagster dagit pandas virtualenv matplotlib requests --upgrade
Crie um novo projeto Dagster:</p>

<p>
bash
Copy code
dagster project scaffold --name <nome_do_projeto>
Instale as dependências do projeto dentro da pasta:</p>

<p>
bash
Copy code
pip install -e ".[dev]"
Configure a variável de ambiente DAGSTER_HOME com o caminho do projeto.</p>

<p>
Inicie o servidor Dagster:</p>

<p>
bash
Copy code
dagster dev
Acesse o Dagit no navegador e explore o pipeline.</p>

<p>
Quando quiser parar o servidor Dagster, pressione CTRL + C.</p>

<p>
Conclusão
Parabéns! Você criou um projeto de crawler usando Scrapy e orquestrou-o com Dagster. Isso demonstra como criar pipelines confiáveis e escalonáveis para processamento de dados.</p>

<p>
javascript
Copy code</p>

<p>
Certifique-se de preencher `<nome_do_projeto>`, `<nome_do_spider>`, `<url_do_site>`, `<nome_do_arquivo>` com os valores específicos do seu projeto. Este exemplo fornece uma visão geral das etapas necessárias para criar um projeto de crawler com Scrapy e orquestrá-lo usando Dagster.</p>


