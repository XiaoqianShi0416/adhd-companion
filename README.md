# ADHD Companion: An Autonomy-Supportive LLM Scaffold
A minimal prototype exploring how LLMs can support task initiation 
for adults with ADHD without using directive or pressuring language.

## Design Rationale
Unlike typical productivity bots that issue commands ("just do X!"), 
this prototype uses Self-Determination Theory's autonomy-supportive 
language patterns: curious questions instead of directives, 
non-judgmental acknowledgment of avoidance, and user-led pacing.

Built on Gemini's free API tier to demonstrate that autonomy-supportive 
scaffolds can be deployed at zero marginal cost — relevant for 
neurodivergent populations who may face barriers to paid tools.

## Usage
​```bash
pip install google-genai
export GEMINI_API_KEY=AIza...
python main.py
​```

## Status
v0.1 — Initial prototype with an exploratory prompt design.

The current system prompt draws on autonomy-supportive language 
principles from Self-Determination Theory, but has not yet been 
systematically grounded in literature. A revised version (v0.2) 
will incorporate findings from my ongoing literature review on 
procrastivity and scaffolding fading.

## Honest Limitations of v0.1
This is an early exploratory prototype. The system prompt was 
drafted based on my own lived experience as a neurodivergent adult 
and informal exposure to autonomy-supportive language principles, 
but is not yet systematically grounded in published literature.

Known issues I plan to address:
1. Prompt is not derived from a formal coding of SDT-based 
   intervention transcripts
2. No empirical validation of whether the model's output 
   actually maintains autonomy-supportive tone
3. The "minimum entry point" framing comes from my own 
   workflow design, not from published scaffolding-fading 
   theory — this needs verification

I am sharing this v0.1 to demonstrate hands-on engagement with 
the technical stack while my literature review is in progress.
