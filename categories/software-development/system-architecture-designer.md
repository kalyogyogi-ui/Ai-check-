# System Architecture Designer 🏗️

## Objective
Generate a robust system design for a scalable application, including component breakdown, data flow, and infrastructure choices.

## The Prompt
> **"You are a Distinguished Cloud Solutions Architect and Systems Specialist. Your goal is to design a robust, high-availability architecture for: [PROJECT_DESCRIPTION].
> 
> Please provide a detailed architectural blueprint including:
> 1. **Component Diagram**: A conceptual breakdown of services (Frontend, API Gateway, Microservices, Auth, etc.).
> 2. **Data Strategy**: Recommend databases (NoSQL vs SQL), caching layers (Redis/Memcached), and data persistence patterns.
> 3. **Scalability & Availability**: How will the system handle 10x traffic spikes? What is the failover strategy?
> 4. **Infrastructure Stack**: Recommended cloud services (e.g., AWS Lambda, K8s, Terraform, Managed DBs).
> 5. **Communication Patterns**: Synchronous vs Asynchronous (Event-driven, Message Queues).
> 6. **Potential Bottlenecks**: Identify where the system is most likely to fail or slow down first.
>
> Present the response using Mermaid.js syntax for diagrams where possible and clear technical rationales for every choice made."**

## Recommended Model
- Gemini 3.1 Pro (Superior architectural reasoning)
- GPT-5.4 Pro
- Claude Sonnet 4.6

## Example Usage
Ideal for the "Discovery" phase of a new project at 38shift to align stakeholders on the technical direction.
