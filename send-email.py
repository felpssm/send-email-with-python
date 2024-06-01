from email.message import EmailMessage
import ssl
import smtplib

servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
servidor_email.starttls()

meu_email = "" #seu email
senha_gerada = "" #sua senha, ou gere uma no gmail, ative a verificação em duas etapas para poder gerar
destinatario_email = "" #email do destinatario
assunto = "Testando python" #assunto
body = """
Enviando email utilizando Python
"""

em = EmailMessage()

em['From'] = meu_email
em['to'] = destinatario_email
em['subject'] = assunto
em.set_content(body)

context = ssl.create_default_context() #criando um contexto SSL seguro

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha_gerada)
    smtp.sendmail(meu_email, destinatario_email,
                  em.as_string())
    