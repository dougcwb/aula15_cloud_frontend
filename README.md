- Criar o git `gh repo create my-project --public --clone` (este repositório)
    * Criar o arquivo `index.html`
- Criar um AWS Amplify
    * Adicionar o repositório do Git criado no passo anterior
- Criar um DynamoDB só com nome da tabela e o ID
    * Copiar o nome do endereço do dynamo
- Criar uma Lambda Function com o codigo `lambda_code.py`
    * ir em segurança e adicionar uma nova política para permitir o dynamo (colar o endereço do dynamo)
- Criar uma trigger (Gateway API > Rest API)
    * Criar um método lambda criado nessa aula
    * Enable Cors