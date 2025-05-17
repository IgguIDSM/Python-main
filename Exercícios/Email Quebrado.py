from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
import smtplib;

# Objeto de Mensagem
msg = MIMEMultipart();
texto = "Realização do Exercício da Faculdade!"
# PArametros
senha = "@Brasil2018";
msg["From"] = "saintstalles@gmail.com";
msg["To"] = "miltonantonio@97hotmail.com";
msg["Subject"] = "Exercício Email Autônomo";
# Cria o Corpo da mensagem
msg.attach(MIMEText(texto,"plain"));
# Cria o Servidor
server = smtplib.SMTP("smtp.gmail.com:587");
server.starttls();
# Login para Envio
server.login(msg["From"],senha);
# Envio
server.sendmail(msg["From"],msg["To"],msg.as_string());
# Encerra o servidor
server.quit();
print("Mensagem enviada com sucesso!");