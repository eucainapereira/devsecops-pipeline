# 🔒 DevSecOps Pipeline — Secure CI/CD com GitHub Actions

[![DevSecOps Pipeline](https://github.com/SEU_USUARIO/devsecops-pipeline/actions/workflows/pipeline.yml/badge.svg)](https://github.com/SEU_USUARIO/devsecops-pipeline/actions/workflows/pipeline.yml)
[![Security Rating](https://img.shields.io/badge/Security-DevSecOps-green?logo=github-actions)](https://github.com/SEU_USUARIO/devsecops-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🎯 O Problema

Apps chegam em produção com **vulnerabilidades conhecidas** porque:

- Segurança é verificada **manualmente** (ou nunca)
- Dependências desatualizadas passam despercebidas
- Segredos (passwords, tokens) são commitados no código
- Containers são buildados a partir de imagens cheias de CVEs
- O time de Dev e o time de Sec trabalham **separados**

---

## 💡 A Solução: DevSecOps

> **"Shift Left Security"** — mover a verificação de segurança para o início do ciclo de desenvolvimento

Esta pipeline integra **4 camadas de análise de segurança** automáticas que executam a cada `git push`, bloqueando o deploy se qualquer vulnerabilidade crítica for detectada.

---

## 🛠️ Arquitetura da Pipeline

```
git push
    │
    ▼
┌──────────────────────────────────────────────────┐
│              🔒 DevSecOps Pipeline                │
│                                                  │
│  ┌─────────────┐  ┌─────────────┐               │
│  │ 🔍 SAST     │  │ 📦 SCA      │               │
│  │  (Bandit)   │  │  (Safety)   │               │
│  └──────┬──────┘  └──────┬──────┘               │
│         │                │                       │
│  ┌──────▼──────┐  ┌──────▼──────┐               │
│  │ 🔑 Secrets  │  │ 🐳 Container│               │
│  │  (Gitleaks) │  │  (Trivy)    │               │
│  └──────┬──────┘  └──────┬──────┘               │
│         │                │                       │
│         └────────┬────────┘                      │
│                  │                               │
│          ┌───────▼───────┐                       │
│          │  Security Gate│                       │
│          │  ✅ PASS ou   │                       │
│          │  ❌ BLOCK     │                       │
│          └───────┬───────┘                       │
│                  │                               │
│          ┌───────▼───────┐                       │
│          │  🚀 Deploy    │                       │
│          │  (se seguro)  │                       │
│          └───────────────┘                       │
└──────────────────────────────────────────────────┘
```

---

## 🔧 Ferramentas Utilizadas

| Ferramenta | Tipo | O que detecta |
|---|---|---|
| **Bandit** | SAST | Vulnerabilidades no código Python (XSS, SQL Injection, Command Injection, segredos hardcoded) |
| **Safety** | SCA | Dependências Python com CVEs conhecidas |
| **Gitleaks** | Secrets | Tokens, passwords, API keys commitadas no repositório |
| **Trivy** | Container | CVEs em pacotes da imagem Docker (OS + libs) |
| **GitHub Actions** | Orquestração | CI/CD automatizado com jobs paralelos |

---

## 📁 Estrutura do Projeto

```
devsecops-pipeline/
├── 📁 .github/
│   └── 📁 workflows/
│       └── pipeline.yml        # Pipeline principal
├── 📁 app/
│   ├── main.py                 # App Flask (com vulnerabilidades intencionais)
│   ├── requirements.txt        # Dependências Python
│   └── Dockerfile              # Imagem Docker
├── .bandit                     # Configuração do Bandit
├── .gitignore                  # Arquivos ignorados
└── README.md                   # Este arquivo
```

---

## 🚨 Vulnerabilidades Intencionais (Fins Educacionais)

A aplicação contém falhas **propositais** para o Bandit detectar:

| Vulnerabilidade | Localização | Severidade |
|---|---|---|
| **XSS** (Cross-Site Scripting) | `/login` endpoint | HIGH |
| **Command Injection** | `/ping` endpoint | HIGH |
| **Hardcoded Secret** | `SECRET_KEY` | MEDIUM |
| **Debug Mode** | `app.run(debug=True)` | MEDIUM |

> ⚠️ **NUNCA use este código em produção!** O objetivo é demonstrar como a pipeline detecta essas falhas.

---

## ⚙️ Como Usar

### 1. Fork/Clone este repositório

```bash
git clone https://github.com/SEU_USUARIO/devsecops-pipeline
cd devsecops-pipeline
```

### 2. Push para a branch main

```bash
git add .
git commit -m "feat: adicionar pipeline DevSecOps"
git push origin main
```

### 3. Acompanhar no GitHub Actions

Acesse: `https://github.com/SEU_USUARIO/devsecops-pipeline/actions`

---

## 📊 Resultado Esperado da Pipeline

### ✅ Jobs que passam:
- SAST lista as vulnerabilidades encontradas (relatório detalhado)
- Safety verifica dependências

### ❌ Jobs que bloqueiam o deploy:
- Trivy falha com `--exit-code 1` se encontrar **HIGH** ou **CRITICAL**
- O job `deploy` só executa se **TODOS** os jobs anteriores passarem

---

## 📸 Exemplos de Saída

### Bandit detectando XSS:
```
Issue: [B703:django_mark_safe] Potential XSS on mark_safe function.
Severity: HIGH   Confidence: HIGH
Location: app/main.py:line 27
```

### Trivy bloqueando deploy:
```
CRITICAL: 3
HIGH:     12

aquasec/trivy image --exit-code 1 --severity HIGH,CRITICAL app-secure
exit code: 1
ERROR: Process completed with exit code 1.
```

---

## 🎓 Aprendizados

- **Shift Left**: Segurança testada em cada commit, não só antes do release
- **Security as Code**: Política de segurança versionada junto com o código
- **Fail Fast**: Pipeline quebra imediatamente ao detectar risco crítico
- **Relatórios**: Artefatos gerados automaticamente para auditoria

---

## 📚 Referências

- [OWASP Top 10](https://owasp.org/Top10/)
- [Bandit Docs](https://bandit.readthedocs.io/)
- [Trivy Docs](https://aquasecurity.github.io/trivy/)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [GitHub Actions Security](https://docs.github.com/en/actions/security-guides)

---

*Desenvolvido para fins educacionais no contexto de estudos em DevSecOps* 🔒
