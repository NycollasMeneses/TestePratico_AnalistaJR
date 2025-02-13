#imagem base do Python
FROM python:3.9
#diretório no contêiner
WORKDIR /app
# Copia os arquivos do projeto para dentro do contêiner
COPY . .
# Instala as dependências da API
RUN pip install --no-cache-dir -r requirements.txt
# Expõe a porta 5000 (onde o Flask rodará, pode ser outra porta tambem)
EXPOSE 5000
# Define o comando para rodar a aplicação
CMD ["python", "WebFrameworks.py"]