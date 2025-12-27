# Encrypted Multi-Tenant Enterprise RAG Platform
##### Zero-Trust AI Search for Confidential Documents

- No plaintext embeddings • No metadata leaks • No prompt exposure
- Enterprise-grade Retrieval-Augmented Generation (RAG) designed for highly confidential data.

<img width="1536" height="1024" alt="ChatGPT Image Dec 24, 2025, 10_00_49 PM" src="https://github.com/user-attachments/assets/8b166064-dc53-4f91-af26-1ad4bf56bbd7" />

## The Problem

Enterprises want to use AI for searching and reasoning over sensitive documents such as:

- Contracts & legal agreements
- Internal emails and policies
- Pricing sheets & negotiation records
- Product designs & intellectual property
- Compliance, audit & regulatory documents

However, traditional RAG systems are fundamentally unsafe:

- Embeddings are invertible → original content can be reconstructed
- Vector databases store embeddings in plaintext
- Metadata leaks business context
- Prompts expose proprietary information to LLMs
- Multi-tenant systems risk cross-organization data leakage

Because of this, law firms, governments, defense organizations, and R&D teams cannot safely adopt RAG.

## Our Solution

This project introduces a fully encrypted, multi-tenant, zero-trust RAG platform that allows enterprises to use AI without ever exposing confidential data.

#### Core Idea
##### AI search should work even if the database, infrastructure, or operator is compromised.

We achieve this by ensuring that:

- Embeddings are encrypted before storage
- Metadata is encrypted
- Vector similarity operates on protected representations
- Prompts are privacy-aware
- LLMs never see raw documents
- Only the final answer is revealed

## High-Level Architecture
User

 ↓ (JWT)
 
Tenant Gateway (Zero-Trust)

 ↓
 
Encrypted Query

 ↓
 
Encrypted Vector Search

 ↓
 
Encrypted Context Signals

 ↓
 
Secure Prompt Construction

 ↓
 
LLM

 ↓
 
Final Answer Only

<img width="1536" height="1024" alt="ChatGPT Image Dec 24, 2025, 10_07_33 PM" src="https://github.com/user-attachments/assets/02da228b-654b-44c8-8cbb-56795b525685" />

###### At no point are documents, embeddings, or metadata exposed in plaintext.

## Security-First Design Principles
### 1. Zero-Trust by Default

- Every request is authenticated
- No service trusts the frontend
- JWT is verified at the gateway
- Tenant identity is enforced end-to-end

### 2. Cryptographic Tenant Isolation

- Each tenant has its own encryption key
- Cross-tenant access is cryptographically impossible
- A breach in one tenant does not affect others

### 3. Encryption-in-Use

- Embeddings are encrypted before storage
- Similarity search operates on protected representations
- No decrypt-then-search pattern

### 4. Answer-Only Output

- LLM never sees raw documents
- Prompts are privacy-aware
- Only the final AI answer is returned

### Key Features

- Encrypted vector storage & search
- Multi-tenant isolated namespaces
- Tenant-scoped encryption keys
- Role-Based Access Control (RBAC)
- Hybrid RAG architecture (search + reasoning)
- Secure prompt engineering
- Observability-ready (Prometheus)
- One-command deployment (Docker Compose)

## Technical Architecture (Services)
#### Service → Responsibility
- Auth Service → Multi-tenant login, JWT issuance, RBAC
- Tenant Gateway → Zero-trust enforcement & request routing
- Ingestion Service → Chunking, embedding, encryption
- Vector Service → Encrypted vector storage & similarity
- RAG Service → Secure retrieval & answer generation
- UI Dashboard → Enterprise-friendly secure interface

## Prototype Scope
#### What Is Fully Implemented

- Multi-tenant authentication & RBAC
- Tenant-isolated encryption
- Encrypted document ingestion
- Encrypted vector similarity search
- Secure RAG orchestration
- Enterprise UI demo

#### What Is Simulated (Clearly Documented)

- HSM / KMS (keys are swappable)
- Enterprise OAuth / SSO
- Production-grade cryptographic similarity

## Threat Model
##### Threat	Mitigation
- Vector DB breach → Encrypted embeddings, no inversion
- Cross-tenant leakage → Tenant-scoped keys + gateway
- Prompt injection → Secure prompt design
- Insider threat → Zero plaintext storage
- LLM data leakage → Answer-only output

➡️ Full analysis in /docs/threat-model.md

<img width="1536" height="1024" alt="ChatGPT Image Dec 24, 2025, 09_52_57 PM" src="https://github.com/user-attachments/assets/f7d14aee-a14b-404e-8a7f-2176356caf06" />

## One-Command Run
- cd infra
- docker compose up --build

#### This launches:

- Auth Service → 8001
- Tenant Gateway → 8002
- Ingestion Service → 8003
- Vector Search → 8004
- RAG Service → 8005
- UI Dashboard → 3000

### Demo Instructions

###### 1.Open UI:
- http://localhost:3000

###### 2.Login with demo credentials:
- Username: alice
- Password: alice123

###### 3.Ask a question about confidential documents

###### 4.Observe:
- No documents shown
- No embeddings visible
- Only final answer returned

#### What You Will See

- Clean enterprise UI
- Explicit security messaging
- Zero exposed internals
- End-to-end encrypted pipeline
- Clear real-world applicability

### Target Users & Impact

- Law firms & legal teams
- Manufacturing & R&D companies
- Government & defense organizations
- Auditing & compliance agencies

This platform enables AI adoption where it was previously impossible.

### Why This Project Is Different
#### Traditional RAG →	This Platform
- Plaintext embeddings → Encrypted embeddings
- DB breach = data leak → DB breach = useless data
- Weak tenant isolation → Cryptographic isolation
- LLM sees documents → LLM sees signals only
- Unsafe for enterprise → Enterprise-deployable

## Scalability & Production Readiness

- Stateless services
- Horizontal scaling
- Replaceable vector backend
- KMS / HSM ready
- Audit-friendly architecture

## Documentation

- Architecture → /docs/architecture.md
- Threat Model → /docs/threat-model.md
- Demo Script → /docs/demo-script.md

##### Disclaimer

This is a research-grade prototype designed to demonstrate:

- Secure enterprise RAG architecture
- Encrypted vector search principles
- Zero-trust AI system design

## Final Note
This project proves that AI can reason over confidential enterprise data without ever exposing it — even under full system compromise.
