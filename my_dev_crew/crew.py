import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.llms import cache as crewai_cache
from crewai.project import CrewBase, agent, crew, task

load_dotenv()
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Disables cache breakpoints for Groq and other strict OpenAI-compatible APIs
crewai_cache.mark_cache_breakpoint = lambda msg: msg

@CrewBase
class MyDevCrew():
    """My local custom software development crew"""

    # Define Custom Model Endpoints Securely using .env

    # 1. Cloudflare Workers AI - Llama 3.1 8B Fast - 10k neuron limit daily
    _cf_account_id = (os.getenv("CLOUDFLARE_ACCOUNT_ID") or "").strip()
    cloudflare_llm = LLM(
        model="@cf/meta/llama-3.1-8b-instruct-fast",
        custom_openai=True,
        base_url=f"https://api.cloudflare.com/client/v4/accounts/{_cf_account_id}/ai/v1",
        api_key=(os.getenv("CLOUDFLARE_API_KEY") or "").strip(),
    )

    # 2. Groq AI - GPT-OSS 120B
    groq_logic_llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY").strip(),
        extra_headers={}
    )

    # 3. Groq AI - Qwen 3.8 27B
    groq_qa_llm = LLM(
        model="groq/qwen/qwen3.8-27b",
        api_key=os.getenv("GROQ_API_KEY").strip(),
        extra_headers={},
        max_tokens=512,
    )

    # 4. Google Gemini 3.5 Flash-Lite
    gemini_context_llm = LLM(
        model="gemini/gemini-3.5-flash-lite",
        api_key=os.getenv("GEMINI_API_KEY").strip()
    )


    @agent
    def codebase_architect(self) -> Agent:
        return Agent(config=self.agents_config['codebase_architect'], llm=self.gemini_context_llm, verbose=True)

    @agent
    def lead_developer(self) -> Agent:
        return Agent(config=self.agents_config['lead_developer'], llm=self.groq_logic_llm, verbose=True)

    @agent
    def quality_assurance(self) -> Agent:
        return Agent(config=self.agents_config['quality_assurance'], llm=self.groq_qa_llm, verbose=True)

    @agent
    def documentation_assistant(self) -> Agent:
        return Agent(config=self.agents_config['documentation_assistant'], llm=self.cloudflare_llm, verbose=True)

    @task
    def analyze_requirements_task(self) -> Task:
        return Task(config=self.tasks_config['analyze_requirements_task'])

    @task
    def write_code_task(self) -> Task:
        return Task(config=self.tasks_config['write_code_task'])

    @task
    def review_code_task(self) -> Task:
        return Task(config=self.tasks_config['review_code_task'])

    @task
    def compile_docs_task(self) -> Task:
        return Task(config=self.tasks_config['compile_docs_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential, 
            verbose=True,
            cache=False
        )