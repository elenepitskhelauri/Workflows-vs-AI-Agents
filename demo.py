"""NEXLEVR Quest 3: fixed workflows versus decision-making agents.

Educational simulation; no external APIs or actual customer data.
"""
from dataclasses import dataclass


def onboarding_workflow(employee: str) -> list[str]:
    """A deterministic, fixed sequence for each new employee."""
    return [
        f"Create account for {employee}",
        "Assign mandatory training",
        "Send welcome email",
        "Notify HR that onboarding is complete",
    ]


@dataclass
class SupportResult:
    category: str
    action: str
    needs_human: bool


def support_decision_agent(message: str) -> SupportResult:
    """A constrained, rule-based stand-in for an agent; no LLM reasoning."""
    message = message.lower()
    if any(term in message for term in ("refund", "charged twice", "billing")):
        return SupportResult("billing", "Create a billing review ticket", True)
    if any(term in message for term in ("password", "login", "sign in")):
        return SupportResult("account access", "Send account recovery instructions", False)
    if any(term in message for term in ("delivery", "shipment", "tracking")):
        return SupportResult("shipping", "Request an order ID for tracking", False)
    return SupportResult("unclassified", "Ask for clarification or escalate", True)


def hybrid_news_workflow(articles: list[dict]) -> list[dict]:
    """Fixed collection/filter/format steps with a simple adaptive topic choice."""
    selected = [a for a in articles if a.get("title") and a.get("url")][:5]
    digest = []
    for article in selected:
        title = article["title"]
        topic = "AI" if "ai" in title.lower().split() else "technology"
        digest.append({
            "title": title,
            "source": article["url"],
            "post_idea": f"Discuss how {topic} affects businesses: {title}",
        })
    return digest


def main() -> None:
    print("\n1) FIXED WORKFLOW — Employee onboarding")
    for i, step in enumerate(onboarding_workflow("Alex"), 1):
        print(f"  {i}. {step}")

    print("\n2) RULE-BASED AGENT PROTOTYPE — Customer support")
    for question in ("I was charged twice", "I forgot my password", "Where is my delivery?"):
        result = support_decision_agent(question)
        print(f"  Customer: {question}")
        print(f"  Decision: {result.category} | {result.action} | Human review: {result.needs_human}")

    print("\n3) HYBRID WORKFLOW — Daily news digest (sample data)")
    sample_articles = [
        {"title": "AI tools reshape office workflows", "url": "https://example.com/sample-ai"},
        {"title": "New cloud infrastructure practices", "url": "https://example.com/sample-cloud"},
    ]
    for item in hybrid_news_workflow(sample_articles):
        print(f"  • {item['title']}\n    Source: {item['source']}\n    Idea: {item['post_idea']}")
    print("\nNote: Example.com URLs are illustrative, not live news sources.")


if __name__ == "__main__":
    main()
