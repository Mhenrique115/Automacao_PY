
# Automação com PyAutoGUI

Este projeto foi desenvolvido para automatizar tarefas repetitivas e otimizar processos no trabalho, principalmente nas demandas que exigem muito tempo, como o cadastramento de produtos ou clientes.

A ideia principal é utilizar a biblioteca `pyautogui` para realizar ações automatizadas, como cliques e digitação, em coordenadas específicas na tela. Isso permite que tarefas repetitivas sejam realizadas de forma mais eficiente, economizando tempo e reduzindo erros.

## Funcionalidade

### 1. Automação de Cliques e Digitação
O script é capaz de simular cliques e digitação no computador. Por exemplo, se for necessário cadastrar vários clientes, basta colocar os nomes dos clientes em um arquivo `.txt` e o script irá automaticamente escrever esses dados nos campos apropriados.

### 2. Utilização de Coordenadas do Mouse
Com o auxílio do `pyautogui`, você pode automatizar qualquer tarefa que envolva cliques na tela. O script permite que o usuário defina as coordenadas de onde os cliques devem acontecer e o que deve ser digitado.

## Como Rodar

### Requisitos

- Python 3.x
- Bibliotecas necessárias:
    - `pyautogui`
    - `mouseinfo`

### Instalando as dependências

1. Primeiro, instale as bibliotecas necessárias:

```bash
pip install pyautogui
pip install mouseinfo
```

2. Clone ou baixe este repositório para a sua máquina.

3. Prepare um arquivo `.txt` com os dados que você deseja automatizar (por exemplo, um arquivo com a lista de clientes).

### Executando o Script

1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório onde o script foi salvo.

3. Execute o script com o seguinte comando:

```bash
python nome_do_script.py
```

O script irá automaticamente começar a realizar as ações, clicando e digitando nos campos necessários de acordo com as coordenadas predefinidas no código.



# Robô de Envio de E-mail e Automação de Tarefas

## Robô de Envio de E-mail

O robô de envio de e-mail foi criado para automatizar o processo de envio de e-mails com anexos. Utilizando a biblioteca **smtplib**, o script envia e-mails via servidor SMTP do Gmail, e com a ajuda da **EmailMessage**, é possível formatar o corpo do e-mail em HTML, permitindo incluir conteúdo enriquecido como imagens, links, e formatação personalizada.

### Funcionamento:

1. **Configuração do E-mail:**
   O script começa configurando as credenciais do e-mail de remetente, o arquivo a ser anexado e o conteúdo HTML do corpo do e-mail.
   
2. **Criação do E-mail:**
   O corpo do e-mail é configurado em formato HTML. Isso permite que o e-mail inclua parágrafos formatados, imagens e links, proporcionando uma aparência mais profissional para o conteúdo enviado.
   
3. **Anexação de Arquivo:**
   O arquivo que será enviado (por exemplo, um arquivo Excel ou PDF) é aberto e anexado ao e-mail para ser enviado ao destinatário.
   
4. **Envio do E-mail:**
   O script se conecta ao servidor SMTP do Gmail, autentica o usuário e envia o e-mail com o arquivo em anexo.

---

## Como os Scripts Podem Ser Combinados

Quando os dois scripts são combinados, você tem uma solução totalmente automatizada que pode realizar tarefas repetitivas como a geração de arquivos e o envio desses arquivos por e-mail de maneira eficiente e sem intervenção manual.

### Processo de Combinação:

1. **Geração de Arquivo:**
   O primeiro script utiliza a biblioteca **PyAutoGUI** para interagir com a interface gráfica do sistema, realizando cliques e escrevendo textos automaticamente. Isso pode ser útil para preencher formulários, gerar relatórios ou qualquer outra tarefa repetitiva. Por exemplo, ele pode preencher uma lista de clientes em uma planilha ou gerar documentos de forma automática.

2. **Envio Automático de E-mail:**
   Após a geração do arquivo, o segundo script é responsável por enviar esse arquivo como anexo para um ou mais destinatários. Ele pode ser configurado para enviar um e-mail HTML personalizado e incluir o arquivo gerado no corpo da mensagem.

### Integração dos Scripts:

A integração pode ser feita de forma simples, onde o segundo script de envio de e-mail é executado logo após o primeiro script gerar o arquivo. Essa combinação elimina a necessidade de realizar essas tarefas manualmente, economizando tempo e aumentando a produtividade.

Dessa forma, com a combinação dos dois scripts, você pode automatizar completamente o processo de criação de arquivos e envio desses arquivos por e-mail, o que é especialmente útil para relatórios periódicos, comunicação com clientes ou envio de documentos importantes.

### Personalização

Você pode personalizar o script para realizar diferentes tarefas, basta ajustar as coordenadas dos cliques e o texto a ser digitado no código.



## Contato

Se você tiver alguma dúvida ou sugestão, pode entrar em contato comigo através dos seguintes canais:

- **LinkedIn:** [Matheus Henrique](https://www.linkedin.com/in/matheushenrique1504/)
- **Instagram:** [@mhenrique36](https://www.instagram.com/mhenrique36/?next=%2F)
