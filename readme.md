# Projeto: Simulações Educativas — Ransomware & Keylogger (seguro)

**Aviso de segurança:** Este repositório contém apenas simulações e ferramentas educativas. Não capture teclas em máquinas reais nem rode códigos maliciosos. Use uma VM isolada e arquivos de teste. Nunca execute scripts em computadores de produção.

## Objetivo
Demonstrar, de forma controlada e educativa, conceitos de:
- Criptografia usada por ransomwares (criptografar/descriptografar arquivos de teste).
- Comportamento de captura de entrada (simulação de logs de teclas).
- Estratégias de defesa: detecção, mitigação e boas práticas.

## Conteúdo
- `scripts/safe_encryptor.py` — script educativo que encripta/desencripta arquivos apenas na pasta `test_files/`.
- `scripts/simulate_keylog.py` — gera um arquivo de log sintético que simula um keylogger para fins de análise (não captura teclado).
- `REPORT.md` — documentação das reflexões, medidas de defesa e resultados dos testes.
- `images/` — capturas e diagramas.

## Como usar (resumo)
1. Crie a pasta `test_files/` e adicione arquivos de teste (.txt).
2. Instale dependências: `pip install -r requirements.txt`.
3. Execute (apenas para fins educativos) `python scripts/safe_encryptor.py --encrypt` (o script pede confirmação).
4. Use `python scripts/simulate_keylog.py` para gerar logs sintéticos.
5. Documente suas observações em `REPORT.md`.

## Defesa e mitigação (resumo)
- Backup offline e versionado.
- EDR/antivírus com heurística.
- Least privilege para usuários.
- Treinamento de conscientização e phishing.
- Isolamento e sandboxing para análise.

Get-ChildItem
# ou
ls