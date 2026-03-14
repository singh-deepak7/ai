## Modern AI Systems — Concise Study Notes

### 1. Tokenization

- Converts raw text → tokens (subwords/characters).

- Each token mapped to an integer ID.

- Common method: Byte Pair Encoding (BPE).

- Example: walking → walk + ing.

- Required because neural networks process numbers, not text.

- **Key idea:** Text → Tokens → IDs → Model input.

### 2. Text Decoding

- LLM outputs a probability distribution for the next token.

- Decoding methods:

    - Greedy: Pick highest probability (deterministic).

    - Top-p (nucleus) sampling: Sample from smallest token set whose cumulative probability ≥ p.

    - Sampling adds creativity & diversity.

 - **Key tradeoff:** Determinism vs Creativity.

### 3. Prompt Engineering

- Steering model behavior without retraining.

- Strong prompt includes:

    - Clear task

    - Constraints

    - Output format

- Techniques:

    - **Few-shot prompting** → Provide examples.

    - **Chain-of-thought (CoT)**- → Ask for step-by-step reasoning.

- Why important?

    - Fast

    - Cheap

    - Highly practical in real systems

### 4. Multi-Step AI Agents

- LLM + Tools + Memory + Loop.

- Agent cycle:

   - Plan

    - Call tool

    - Observe result

    - Repeat

- Enables:

    - Web browsing

    - Code execution

    - Multi-step workflows

- **LLM alone** = *text generator*.
- **Agent** = *decision-making system*.

### 5. Retrieval-Augmented Generation (RAG)

#### Problem: LLM knowledge can be outdated or incorrect.

#### Solution:

    1. Retrieve relevant documents.

    2. Provide them to LLM.

    3. Generate grounded response.

- **Benefit**: Reduces hallucinations and improves factual accuracy.

- **Formula**:
*User Query → Retriever → Context → LLM → Answer*

### 6. Reinforcement Learning from Human Feedback (RLHF)

- Improves alignment with human preferences.

- Process:

    1.  Model generates multiple answers.

    2. Humans rank them.

    3. Reward model learns preferences.

    4. RL updates LLM toward higher-reward outputs.

**Optimizes for**: *Helpfulness, clarity, safety — not just probability.*

### 7. Variational Autoencoder (VAE)

- Generative model with:

    - *Encoder → Input → Latent space*

    - *Decoder → Latent → Output*

- Trained to:

    - Reconstruct input

    - Learn data distribution

- Used in:

    - Text-to-image systems

    - Latent compression

**Core idea**: *Learn compressed representation of data.*

### 8. Diffusion Models

- Generate data by reversing noise.

    - Training:

        - Add noise gradually.

        - Train model to predict noise.

    - Inference:

       - Start with pure noise.

       - Remove noise step-by-step.

    - Used in:

       - Image generation

       - Video generation

**Core idea:** *Noise → Structure.*

### 9. Low-Rank Adaptation (LoRA)

- Efficient fine-tuning method.

- Instead of updating all weights:

    - Freeze original weights.

    - Add small low-rank matrices.

    - Train only those.

- Benefit:

    - Much fewer parameters

    - Faster & cheaper fine-tuning


#
# 🔥 Big Picture Architecture View

### Most modern AI systems combine:

- Tokenization

- LLM

- Decoding strategy

- Prompt engineering

- RAG (for knowledge grounding)

- RLHF (for alignment)

- Agents (for actions)

- Diffusion/VAE (for media generation)

- LoRA (for domain adaptation)