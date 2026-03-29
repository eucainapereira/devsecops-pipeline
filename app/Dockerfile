# ─────────────────────────────────────────────
#  Imagem base — Python 3.9 slim (menor ataque)
# ─────────────────────────────────────────────
FROM python:3.9-slim

# Metadados da imagem
LABEL maintainer="devsecops-demo"
LABEL description="Aplicação com vulnerabilidades intencionais para fins educacionais"

# Usuário não-root (boas práticas de segurança)
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copiar dependências primeiro (melhor cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Trocar para usuário não-root
USER appuser

# Expor porta da aplicação
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

CMD ["python", "main.py"]
