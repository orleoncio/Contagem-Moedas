# Contagem de Moedas com Visão Computacional

Projeto de **Processamento Digital de Imagens (PDI)** e **Visão Computacional** em Python, com foco na identificação e contagem de moedas presentes em uma fotografia.

A abordagem utiliza a **Transformada Circular de Hough**, disponível no OpenCV, para localizar formas aproximadamente circulares na imagem e estimar a quantidade de moedas detectadas.

> **Escopo:** contagem de objetos circulares. A detecção de uma moeda não implica reconhecimento de seu valor monetário.

## Objetivos

- Ler e processar imagens contendo moedas.
- Identificar regiões aproximadamente circulares.
- Contar os círculos detectados.
- Visualizar as detecções sobre a imagem.
- Investigar como os parâmetros do algoritmo afetam os resultados.

## Tecnologias

- **Python** — implementação.
- **OpenCV** — leitura de imagens, pré-processamento e Transformada Circular de Hough.
- **NumPy** — operações numéricas e manipulação dos resultados.
- **Matplotlib** — visualização dos resultados, quando utilizada no notebook.
- **Jupyter Notebook** — execução e análise experimental.

## Funcionamento

```text
Imagem com moedas
       ↓
Conversão para escala de cinza
       ↓
Pré-processamento da imagem
       ↓
Transformada Circular de Hough
       ↓
Coordenadas e raios dos círculos
       ↓
Contagem e visualização das detecções
```

### Detecção de círculos

O método `cv2.HoughCircles()` procura padrões circulares a partir das informações de bordas da imagem. Cada detecção é representada por três valores:

- `x`: coordenada horizontal do centro;
- `y`: coordenada vertical do centro;
- `r`: raio estimado.

Exemplo do núcleo do algoritmo:

```python
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.3,
    minDist=20,
    param1=100,
    param2=30,
    minRadius=20,
    maxRadius=50
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    quantidade = len(circles[0])
    print(f"Moedas detectadas: {quantidade}")
```

Os valores são **parâmetros de exemplo**: devem ser ajustados à resolução da imagem, à distância entre moedas e aos raios esperados.

### Principais parâmetros

| Parâmetro | Função |
|---|---|
| `dp` | Relação entre a resolução da imagem e a do acumulador |
| `minDist` | Distância mínima entre centros detectados |
| `param1` | Limiar superior utilizado na detecção de bordas |
| `param2` | Limiar de decisão para aceitar círculos candidatos |
| `minRadius` | Menor raio procurado |
| `maxRadius` | Maior raio procurado |

Após a detecção, `cv2.circle()` pode desenhar a circunferência e o centro de cada moeda na imagem de saída.

## Como executar

1. Clone o repositório e acesse a pasta do projeto.
2. Crie e ative um ambiente virtual Python.
3. Instale as dependências:

```bash
pip install opencv-python numpy matplotlib jupyter ipykernel
```

4. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

5. Abra o notebook do projeto, configure o caminho da imagem e execute as células em sequência.

> Ajuste os caminhos e nomes de arquivos à estrutura efetiva do seu repositório.

## Testes recomendados

| Cenário | O que observar |
|---|---|
| Moedas separadas, com boa iluminação | Contagem básica |
| Moedas de tamanhos diferentes | Efeito de `minRadius` e `maxRadius` |
| Moedas próximas | Efeito de `minDist` |
| Reflexos e sombras | Falsos positivos e círculos não detectados |
| Moedas parcialmente sobrepostas | Limitações da detecção circular |

## Limitações

- A detecção depende da qualidade da imagem e do ajuste dos parâmetros.
- Objetos circulares que não são moedas podem gerar falsos positivos.
- Moedas sobrepostas, cortadas ou parcialmente ocultas podem não ser identificadas.
- A técnica detecta círculos, mas não determina automaticamente o valor ou a denominação das moedas.

## Possíveis melhorias

- Avaliar a contagem em imagens com diferentes iluminações e fundos.
- Comparar a Transformada de Hough com segmentação e análise de contornos.
- Calibrar os raios para distinguir grupos de tamanhos, quando as condições de captura permitirem.
- Criar um conjunto de imagens anotadas para medir precisão de detecção e erro de contagem.

## Contexto

Projeto de estudo e portfólio para demonstrar fundamentos de detecção de formas, processamento de imagens e ajuste experimental de algoritmos de Visão Computacional.
