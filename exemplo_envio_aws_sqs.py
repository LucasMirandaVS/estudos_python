import boto3

# Criando o Client
sqs = boto3.clent('sqs')

# URL da fila
queue_URL = "inserir a url da fila onde vc quero conectar"

# Enviando a mensagem pra fila 
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Mensagem de exemplo para minha-fila-standard'
)

# Exibindo o ID da mensagem enviada
print(f"Mensagem enviada com sucesso! ID da mensagem: {response['MessageId']}")
