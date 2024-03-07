# Criando um Recurso no Portal Vision Cognitive Azure

## Ideia do projeto:

Por mais que esse projeto utilize a IA VISION da AZURE e consiga ler textos de qualquer imagem, eu a utilizei para ler cupoms fiscais de mercado, assim tornando muito mais fácil a digitalização e a organização dos gastos diários ou mensais com mercado. Por enquanto ele apenas está lendo esses cupoms e atualizando a "outputs" exatamente da forma que ele leu, mas futuramente penso em organizar esses dados conforme descrito acima.

Para utilizar as APIs de visão computacional do Azure, você precisa criar um recurso no portal `portal.vision.cognitive.azure.com`. Aqui está um guia passo a passo:

### 1. Acessar o Portal:

* Acesse o portal `portal.vision.cognitive.azure.com` usando sua conta Microsoft.
* Se for sua primeira vez, aceite os termos de serviço e a política de privacidade.

### 2. Criar um Recurso:

* Clique no botão **+ Criar Recurso**.
* Na caixa de pesquisa, digite "Visão Computacional" e selecione o resultado.
* Preencha os seguintes campos:

    - **Nome do Recurso:** Insira um nome único para o seu recurso.
    - **Assinatura:** Selecione a assinatura do Azure que deseja usar.
    - **Grupo de Recursos:** Crie um novo grupo de recursos ou selecione um existente.
    - **Localização:** Selecione a região mais próxima de você.

* Clique em **Criar**. Aguarde alguns minutos enquanto o recurso é criado.

### 3. Obter Chave de Acesso:

* Navegue até o seu recurso no portal.
* Na seção **Visão Geral**, clique em **Chaves de Acesso**.
* Copie a chave **Primária** ou **Secundária**. Você precisará dela para usar as APIs de visão computacional.

### 4. Testar a API:

![Chaves da API Azure Vision](https://raw.githubusercontent.com/VicLira/azureml-ai900-ocr/main/imgs_readme/chave_azure.png))


* Acesse o portal `dev.azure.com`.
* Crie um novo projeto.
* No menu esquerdo, selecione **+ Novo** > **API**.
* Pesquise por "Visão Computacional" e selecione a API **Computer Vision**.
* Clique em **Criar**.
* Insira a chave de acesso que você copiou no passo anterior.
* Clique em **Testar**.
* Selecione a operação que deseja testar e siga as instruções.

### Recursos Adicionais:

* Quickstart: Azure AI Vision v3.2 GA Read: [quickstart](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/client-library?tabs=linux%2Cvisual-studio&pivots=programming-language-python)

### Resolução de Problemas (insights):

* O que eu mais tive problemas foi colocar imagens na pasta "inputs" e tentar ler as imagens pela propria API da azure, por algum problema eu não consegui ler as imagens diretamente, então a forma que resolvi foi seguindo o "quickstart" e lendo url das imagens, mas para deixar dinâmico, eu fiz um json onde é possivel você inserir link de qualquer imagem, além de ser quantos links forem necessários e ir lendo url por url com um loop.

* Foi bem dificil também entender exatamente quais eram as bibliotecas corretas a serem importadas para o recurso que eu queria utilizar, já que olhando na internet e nas documentações eu encontrei muitas. Porém assim que encontrei o quickstart acima com o mesmo exemplo que eu queria fazer nesse projeto, eu segui essas libs.

**Este foi o guia que crier/utilizei para criar um recurso no portal Vision Cognitive Azure e começar a usar as APIs de visão computacional.**

**Obrigado pela atenção! Com dúvidas meu contato é: victor.liracarlos@gmail.com**
