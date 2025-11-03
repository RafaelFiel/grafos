# 🔗 Aplicações de Grafos
> Projetos práticos de Estrutura de Dados aplicando teoria de grafos em problemas do cotidiano

## 📋 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Projetos Implementados](#-projetos-implementados)
  - [1. Rotas Aéreas entre Aeroportos](#️-1-rotas-aéreas-entre-aeroportos)
  - [2. Rede de Transporte Público](#-2-rede-de-transporte-público)
  - [3. Rede Social de Usuários](#-3-rede-social-de-usuários)
  - [4. Rede de Disciplinas e Pré-requisitos](#-4-rede-de-disciplinas-e-pré-requisitos)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Como Executar](#-como-executar)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Autor](#-autor)

---

## 📘 Sobre o Projeto

Este repositório reúne **quatro projetos práticos** desenvolvidos na disciplina de **Estrutura de Dados**, aplicando o conceito de **grafos** em diferentes contextos do dia a dia.

Cada projeto representa um tipo específico de rede, onde:
- **Vértices** representam elementos (aeroportos, estações, usuários, disciplinas)
- **Arestas** representam conexões (rotas, trajetos, amizades, pré-requisitos)
- **Pesos** indicam métricas relevantes (tempo, distância, força da conexão)

---

## 🚀 Projetos Implementados

### ✈️ 1. Rotas Aéreas entre Aeroportos

**Contexto:** Sistema de voos entre aeroportos  
**Representação:** 
- Vértices = Aeroportos
- Arestas = Rotas aéreas com peso (tempo de viagem)

**Funcionalidades:**
- ✅ Cadastrar e remover aeroportos
- ✅ Adicionar e excluir rotas
- ✅ Verificar conexões entre cidades
- ✅ Calcular menor tempo de viagem (Algoritmo de Dijkstra)

**Localização:** `rotas_voos/`

---

### 🚆 2. Rede de Transporte Público

**Contexto:** Sistema de transporte urbano (ônibus/metrô)  
**Representação:**
- Vértices = Estações
- Arestas = Trajetos com peso (tempo de percurso)

**Funcionalidades:**
- ✅ Adicionar e remover estações
- ✅ Criar conexões entre estações
- ✅ Calcular menor caminho entre pontos (Algoritmo de Dijkstra)
- ✅ Visualizar rede de transporte

**Localização:** `transporte_urbano/`

---

### 🧑‍🤝‍🧑 3. Rede Social de Usuários

**Contexto:** Simulação de rede social  
**Representação:**
- Vértices = Usuários
- Arestas = Relações de amizade (com ou sem peso)

**Funcionalidades:**
- ✅ Adicionar e remover usuários
- ✅ Criar conexões de amizade
- ✅ Verificar se dois usuários estão conectados
- ✅ Sugerir amizades (amigos em comum)
- ✅ Analisar influência por número de conexões

**Localização:** `conexoes_sociais/`

---

### 📚 4. Rede de Disciplinas e Pré-requisitos

**Contexto:** Sistema acadêmico de disciplinas  
**Representação:**
- Vértices = Disciplinas
- Arestas = Dependências (grafo direcionado)

**Funcionalidades:**
- ✅ Adicionar e remover disciplinas
- ✅ Definir vínculos de pré-requisitos
- ✅ Detectar ciclos de dependência
- ✅ Gerar ordem de cursagem (Ordenação Topológica)

**Localização:** `disciplinas_academicas/`

---

## 📁 Estrutura do Repositório

```
grafos/
├── rotas_voos/
│   ├── main.py
│   └── mapa_voos.py
├── transporte_urbano/
│   ├── main.py
│   └── grafo_transporte.py
├── conexoes_sociais/
│   ├── main.py
│   └── rede_social.py
├── disciplinas_academicas/
│   ├── main.py
│   └── sistema_disciplinas.py
└── README.MD
```

---

## 🎮 Como Executar

### Pré-requisitos
- Python 3.x instalado

### Execução

Navegue até a pasta do projeto desejado e execute o arquivo `main.py`:

```bash
# Exemplo: Rotas Aéreas
cd rotas_voos
python main.py

# Exemplo: Transporte Público
cd transporte_urbano
python main.py

# Exemplo: Rede Social
cd conexoes_sociais
python main.py

# Exemplo: Disciplinas
cd disciplinas_academicas
python main.py
```

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Estruturas de Dados:** Grafos (Listas de Adjacência)
- **Algoritmos:** 
  - Dijkstra (menor caminho)
  - Ordenação Topológica
  - Detecção de Ciclos
  - BFS/DFS

---

## 👨‍💻 Autor

**Rafael de Freitas Fiel**  
Disciplina: Estrutura de Dados