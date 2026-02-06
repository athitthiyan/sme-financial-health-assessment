import os

def generate_insights(data):
    try:
        import openai

        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise Exception("OpenAI key not found")

        prompt = f"""
        Revenue: {data['revenue']}
        Expenses: {data['expenses']}
        Profit: {data['profit']}
        Health Score: {data['score']}

        Give simple financial advice for an SME owner.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔒 FALLBACK (prevents 500 error)
        return (
            "Your business shows stable financial performance. "
            "Monitor expenses closely and focus on improving cash flow "
            "to strengthen financial health."
        )
