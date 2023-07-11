import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':

    desired_cashback = 5

    # Send a GET request to the website
    url = "https://www.comparemania.com.br/promocao/cashback/amazon"
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the product elements on the page
    products = soup.find_all(name='p', class_='mb-2 text-center', recursive= True)

    cashback = list()
    # Iterate over each product and extract the information
    for product in products:
        if "cashback" in product.string:
            cashback.append(product.string)

    print("Cashback:", cashback)
    print("----------------------")
    print("Cashback máximo:", cashback[0])
    print("----------------------")
    print("Cashback atingido?:", int(cashback[0][0]) > desired_cashback)


    def enviar_email(destinatario, assunto, mensagem):

        # Configurações do servidor de e-mail
        servidor_smtp = 'smtp.gmail.com'
        porta_smtp = 587
        endereco_email = 'ciranodroid@gmail.com'
        senha = ''

        # Criando o objeto de e-mail
        email = MIMEMultipart()
        email['From'] = endereco_email
        email['To'] = destinatario
        email['Subject'] = assunto

        # Adicionando a mensagem ao corpo do e-mail
        corpo_email = mensagem
        email.attach(MIMEText(corpo_email, 'plain'))

        # Criando a conexão com o servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(endereco_email, senha)

        # Enviando o e-mail
        servidor.sendmail(endereco_email, destinatario, email.as_string())

        # Encerrando a conexão com o servidor SMTP
        servidor.quit()


    # Exemplo de uso
    destinatario = 'belardony@gmail.com'
    assunto = 'Alerta de Cashback - Amazon'
    mensagem = "Você está recebendo esse e-mail pois o cashback desejado na loja Amazon foi atingido: " \
               + str(cashback[0]) +"!"
    enviar_email(destinatario, assunto, mensagem)




    
