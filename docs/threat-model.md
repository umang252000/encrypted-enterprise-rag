# 🔐 Threat Model — Encrypted Multi-Tenant Enterprise RAG

## Objective

This document analyzes realistic attack scenarios against an enterprise RAG system and explains how the architecture mitigates each threat.

The system is designed under the assumption that:
- Infrastructure may be breached
- Databases may be exfiltrated
- Insiders may exist
- LLMs are not fully trusted

---

## Threat 1: Vector Database Breach

### Scenario
An attacker gains full read access to the vector database.

### Risk in Traditional RAG
- Plaintext embeddings are invertible
- Original documents can be reconstructed
- Sensitive data is exposed

### Mitigation in This System
✅ All embeddings are encrypted  
✅ No plaintext vectors exist  
✅ Encrypted similarity search prevents inversion  

**Result:** Database exfiltration yields unusable data.

---

## Threat 2: Cross-Tenant Data Leakage

### Scenario
Tenant A attempts to access Tenant B’s data.

### Risk
- Weak namespace isolation
- Shared vector indices
- Misconfigured access control

### Mitigation
✅ Tenant-scoped encryption keys  
✅ Tenant identity enforced in JWT  
✅ Gateway blocks cross-tenant requests  
✅ Encrypted vectors are tenant-specific  

**Result:** Cross-tenant access is cryptographically impossible.

---

## Threat 3: Prompt Injection & Data Exfiltration

### Scenario
A user crafts a malicious query to force the LLM to reveal sensitive content.

### Risk
- LLM sees raw documents
- Prompt injection leaks data

### Mitigation
✅ LLM never sees raw documents  
✅ Prompts contain encrypted signals only  
✅ Answer-only output policy  

**Result:** Prompt injection cannot extract confidential data.

---

## Threat 4: Insider Threat (DB Admin / Operator)

### Scenario
A privileged insider attempts to inspect stored data.

### Risk
- Plaintext access to documents
- Metadata leakage

### Mitigation
✅ Zero plaintext storage  
✅ Encrypted metadata  
✅ No keys stored with data  

**Result:** Insider access yields no readable information.

---

## Threat 5: Compromised LLM Provider

### Scenario
LLM provider logs or inspects prompts.

### Risk
- Proprietary documents exposed
- Regulatory violations

### Mitigation
✅ Prompts do not contain sensitive data  
✅ No raw document content is sent  
✅ Only abstracted context signals used  

**Result:** LLM provider learns nothing sensitive.

---

## Threat 6: Man-in-the-Middle Attack

### Scenario
Network traffic is intercepted.

### Mitigation
✅ JWT authentication  
✅ Encrypted payloads  
✅ No sensitive plaintext in transit  

**Result:** Intercepted traffic is useless.

---

## Threat Summary Table

| Threat | Impact | Mitigation |
|-----|------|-----------|
| DB breach | Critical | Encrypted embeddings |
| Tenant leakage | Critical | Tenant-scoped crypto |
| Prompt injection | High | Secure prompts |
| Insider threat | High | Zero plaintext |
| LLM leakage | High | Answer-only |
| MITM | Medium | Encrypted transport |

---

## Security Guarantees

- Confidential documents are never exposed
- Embeddings cannot be inverted
- Tenants are cryptographically isolated
- AI reasoning occurs without data leakage

---

## Conclusion

This threat model demonstrates that **secure enterprise RAG is achievable today** when encryption and zero-trust principles are applied end-to-end.

The system remains safe even under worst-case assumptions.