## Overview Diagram


```mermaid
graph TD
    A[Load Data] --> B[Data Cleaning]
    B --> C[Sentiment Analysis]
    C --> D[NLTK - Offline VADER Sentiment Analysis]
    C --> E[Azure OpenAI Integration]
    D --> G[Data Visualization]
    E --> G[Data Visualization]
    G --> H[Rating Distribution]
    G --> I[Sentiment Distribution]
    G --> J[Word Cloud]
    G --> K[Insights Generation]
    K --> L[PandasAI Integration]
    K --> M[Pivot Tables]
    
```


```mermaid
graph TD
    A[Start] --> B[Load Environment Variables]
    B --> C[Initialize Azure OpenAI Client]
    C --> D[Create Chat Completion Request]
    D --> E[Process Response]

    subgraph "Load Environment Variables"
        B1[Load .env File]
        B2[Retrieve Azure OpenAI Endpoint]
        B3[Retrieve Azure OpenAI API Key]
        B4[Retrieve Azure OpenAI API Version]
        B5[Retrieve Azure OpenAI Deployment Name]
        B --> B1
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 --> B5
    end

    subgraph "Initialize Azure OpenAI Client"
        C1[Set Endpoint]
        C2[Set API Key]
        C3[Set API Version]
        C --> C1
        C1 --> C2
        C2 --> C3
    end

    subgraph "Create Chat Completion Request"
        D1[Set Deployment Name]
        D2[Define Messages]
        D --> D1
        D1 --> D2
    end

    subgraph "Process Response"
        E1[Receive Response]
        E2[Handle Output]
        E --> E1
        E1 --> E2
    end