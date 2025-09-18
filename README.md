# 🌸 Generador de Poesía con Ollama

## Descripción General

Este proyecto demuestra cómo utilizar la API de Ollama para generar poesía bilingüe. El ejemplo crea un hermoso poema de cuatro estrofas sobre la primavera en Uruguay, presentado tanto en inglés como en español.

## 🚀 Características

- **Generación de Poesía Bilingüe**: Crea poemas en inglés y español
- **Respuesta en Streaming**: Procesa respuestas en tiempo real desde la API de Ollama
- **Integración con LLM Local**: Utiliza modelos de lenguaje alojados localmente
- **Contexto Cultural**: Incorpora elementos geográficos y culturales específicos

## 📋 Requisitos

```txt
requests>=2.31.0
```

## 🛠️ Configuración

1. **Instalar Ollama** (si no está instalado):
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Descargar el modelo requerido**:
   ```bash
   ollama pull gpt-oss:20b
   ```

3. **Iniciar el servidor Ollama**:
   ```bash
   ollama serve
   ```

4. **Instalar dependencias de Python**:
   ```bash
   uv init
   uv add requests
   ```

## 💻 Implementación del Código
#Modulo para request de cualquier api de LLM
```python
import requests
import json
from typing import Optional, Dict, Any

class OpenAIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.__api_key = api_key
        self.__base_url = base_url
    
    @property
    def api_key(self) -> Optional[str]:
        return self.__api_key
    
    @property
    def base_url(self) -> str:
        return self.__base_url
    
    @api_key.setter
    def api_key(self, value: str):
        if value is not None and not isinstance(value, str):
            raise ValueError("API key must be a string or None.")
        self.__api_key = value
    
    @base_url.setter
    def base_url(self, value: str):
        if not isinstance(value, str) or not value.startswith("http"):
            raise ValueError("Base URL must be a valid URL string.")
        self.__base_url = value
    
    def call(self, data: Dict[str, Any], headers: Optional[Dict[str, str]] = None):

        req_headers = {"Content-Type": "application/json"}
        if self.api_key:
            req_headers["Authorization"] = f"Bearer {self.api_key}"
        if headers:
            req_headers.update(headers)

        response = requests.post(self.base_url, json=data, headers=req_headers, stream=True)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
            return
        
        print("Response received:")
        for line in response.iter_lines():
            if not line:
                continue
            obj = json.loads(line.decode("utf-8"))
            if "response" in obj:
                print(obj["response"], end="")
        print()
```
## 💻 Implementación del Código Cliente
#Cliente
```python
from promptLLM import OpenAIClient

def main():
    url_api_ollama = "http://localhost:11434/api/generate"

    data = {
        "model": "gpt-oss:20b",
        "prompt": "Write a four-stanza poem about spring in the Eastern Republic of Uruguay. In English and Spanish.",
    }

    client = OpenAIClient(base_url=url_api_ollama)

    client.call(data)

if __name__ == "__main__":
    main()
```
## 📖 Salida Generada

**Estrofa 1**  
The eastern breeze awakens the sun, soft and new,  
*El viento del Oriente despierta el sol, suave y nuevo.*  

**Estrofa 2**  
Pampas blush with clover, a green quilt in the dawn,  
*Las pampas se tiñen de trébol, un manto verde al amanecer.*  

**Estrofa 3**  
The Uruguay River hums with life, its banks kissed by spring,  
*El Río Uruguay susurra vida, sus orillas besadas de primavera.*  

**Estrofa 4**  
People laugh, children dance, the air fragrant with hope,  
*La gente ríe, los niños bailan, el aire perfumado de esperanza.*  

## 🔧 Opciones de Configuración

Puedes personalizar la generación modificando estos parámetros:

- **model**: Cambiar el modelo LLM (ej: `llama2`, `mistral`, `codellama`) son mas ligeros...
- **prompt**: Modificar el prompt creativo para diferentes temas
- **temperature**: Controlar la aleatoriedad (agregar al diccionario `data`)
- **max_tokens**: Limitar la longitud de la respuesta (agregar al diccionario `data`)

## 🌟 Casos de Uso

- **Escritura Creativa**: Generar poesía para proyectos artísticos
- **Aprendizaje de Idiomas**: Practicar creación de contenido bilingüe
- **Documentación Cultural**: Crear literatura específica de ubicaciones
- **Integración de APIs**: Plantilla para el uso de la API de Ollama

## 📚 Notas Técnicas

- Utiliza respuesta en streaming para salida en tiempo real
- Maneja el parsing de JSON de respuestas fragmentadas
- Incluye manejo apropiado de errores para fallos de API
- Compatible con varios modelos de Ollama

## 🤝 Contribuciones

Siéntete libre de hacer fork de este proyecto y experimentar con:
- Diferentes estilos y temas de poesía
- Combinaciones adicionales de idiomas
- Mejoras en el manejo de errores
- Mejoras en el formato de salida

---

*Generado con ❤️ usando Ollama y Python*